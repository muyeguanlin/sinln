use mysql::Pool;
use mysql::prelude::*;
use mysql::Row;

pub struct MysqlConnection {
    pool: Pool,
}

impl MysqlConnection {
    pub fn new(url: &str) -> Result<Self, String> {
        Pool::new(url)
            .map(|pool| Self { pool })
            .map_err(|e| e.to_string())
    }

    pub fn execute_query(&self, query: &str) -> Result<Vec<Row>, String> {
        let mut conn = self.pool.get_conn().map_err(|e| e.to_string())?;
        conn.query_iter(query)
            .and_then(|result| result.collect::<Result<Vec<_>, _>>())
            .map_err(|e| e.to_string())
    }

    pub fn get_mysql_version(&self) -> Result<String, String> {
        self.execute_query("SELECT VERSION()")
            .and_then(|rows| {
                rows.into_iter()
                    .next()
                    .and_then(|row| row.get::<String, _>(0))
                    .ok_or_else(|| "No version found".to_string())
            })
    }
}