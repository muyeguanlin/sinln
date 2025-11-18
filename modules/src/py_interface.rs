use crate::mysql_utils::MysqlConnection;
use mysql::Value;
use pyo3::prelude::*;
use pyo3::types::{PyBytes, PyDict, PyList};

#[pyclass]
pub struct PyMysqlConnection {
    inner: MysqlConnection,
}

#[pymethods]
impl PyMysqlConnection {
    #[new]
    pub fn new(url: &str) -> PyResult<Self> {
        MysqlConnection::new(url)
            .map(|conn| Self { inner: conn })
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e))
    }

    pub fn execute_query(&self, py: Python, query: &str) -> PyResult<PyObject> {
        let rows = self
            .inner
            .execute_query(query)
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e))?;

        let py_rows = PyList::empty(py);
        for row in rows {
            let dict = PyDict::new(py);
            for (i, col) in row.columns_ref().iter().enumerate() {
                // 正确用法：直接处理Option
                let value = row.get::<Value, usize>(i).unwrap_or(Value::NULL);
                let py_value = convert_mysql_value(py, value)?;
                dict.set_item(col.name_str(), py_value)?;
            }
            py_rows.append(dict)?;
        }
        Ok(py_rows.into())
    }

    pub fn get_mysql_version(&self) -> PyResult<String> {
        self.inner
            .get_mysql_version()
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(e))
    }
}

fn convert_mysql_value(py: Python, value: Value) -> PyResult<PyObject> {
    match value {
        Value::NULL => Ok(py.None()),
        Value::Bytes(bytes) => {
            // 先克隆 bytes 再使用
            let bytes_clone = bytes.clone();
            String::from_utf8(bytes)
                .map(|s| s.into_py(py))
                .or_else(|_| Ok(PyBytes::new(py, &bytes_clone).into()))
        }
        Value::Int(i) => Ok(i.into_py(py)),
        Value::UInt(u) => Ok(u.into_py(py)),
        Value::Float(f) => Ok(f.into_py(py)),
        Value::Date(y, m, d, h, min, s, _) => {
            Ok(format!("{}-{:02}-{:02} {:02}:{:02}:{:02}", y, m, d, h, min, s).into_py(py))
        }
        _ => Ok(format!("{:?}", value).into_py(py)),
    }
}
