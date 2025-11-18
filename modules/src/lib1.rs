
use mysql::*;
use mysql::prelude::*;
use pyo3::prelude::*;
use pyo3::types::{PyDict, PyList, PyBytes};


/// 获取 MySQL 版本
#[pyfunction]
fn get_mysql_version(url: &str) -> PyResult<String> {
    let pool = Pool::new(url).map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;
    let mut conn = pool.get_conn().map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;
    
    let result: Vec<String> = conn.query_map("SELECT VERSION()", |version| version)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;
    
    Ok(result.join(", "))
}

/// 执行通用查询并返回结果


#[pyfunction]
fn execute_query(py: Python, url: &str, query: &str) -> PyResult<PyObject> {
    let pool = Pool::new(url)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;
    
    let mut conn = pool.get_conn()
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;
    
    let result = conn.query_iter(query)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;
    
    let rows = PyList::empty(py);
    
    for row in result {
        let row = row.map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e.to_string()))?;
        let row_dict = PyDict::new(py);
        
        for (i, col) in row.columns_ref().iter().enumerate() {
            let col_name = col.name_str();
            let value: Value = row.get(i).unwrap_or(Value::NULL);
            
            match value {
                Value::NULL => row_dict.set_item(col_name, py.None())?,
                Value::Bytes(bytes) => {
                    if let Ok(s) = String::from_utf8(bytes.clone()) {
                        row_dict.set_item(col_name, s)?;
                    } else {
                        let py_bytes = PyBytes::new(py, &bytes);
                        row_dict.set_item(col_name, py_bytes)?;
                    }
                },
                Value::Int(i) => row_dict.set_item(col_name, i)?,
                Value::UInt(u) => row_dict.set_item(col_name, u)?,
                Value::Float(f) => row_dict.set_item(col_name, f)?,
                Value::Date(y, m, d, h, min, s, _us) => {
                    let dt = format!("{}-{:02}-{:02} {:02}:{:02}:{:02}", 
                                   y, m, d, h, min, s);
                    row_dict.set_item(col_name, dt)?;
                },
                Value::Time(neg, d, h, m, s, _us) => {
                    let sign = if neg { "-" } else { "" };
                    let dt = format!("{}{} days {:02}:{:02}:{:02}", 
                                   sign, d, h, m, s);
                    row_dict.set_item(col_name, dt)?;
                },
                // 处理其他未明确处理的变体
                _ => {
                    // 使用Debug trait作为最后手段
                    row_dict.set_item(col_name, format!("{:?}", value))?;
                }
            }
        }
        
        rows.append(row_dict)?;
    }
    
    Ok(rows.into())
}



#[pymodule]
fn modules(_py: Python,m: &Bound<'_, PyModule>) -> PyResult<()> {
// fn mysql_pyo3(py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    // m.add_class::<Payment>()?;
    m.add_function(wrap_pyfunction!(get_mysql_version, m)?)?;
    m.add_function(wrap_pyfunction!(execute_query, m)?)?;
    Ok(())
}