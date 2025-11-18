mod mysql_utils;
mod py_interface;

use py_interface::PyMysqlConnection;
use pyo3::prelude::*;
use pyo3::types::PyModule;

#[pymodule]
// fn mysql_pyo3(_py: Python, m: &PyModule) -> PyResult<()> {
fn modules(_py: Python,m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<PyMysqlConnection>()?;
    Ok(())
}