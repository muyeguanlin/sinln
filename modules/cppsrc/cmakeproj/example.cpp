// // python setup.py build_ext --inplace
// // import <iostream>;  // C++23 标准库模块化
// // mkdir build
// // # cd build
// // # cmake ..
// // # cmake --build .
/////////////////////////////////////////////////////////////////////////////////////////////////////

#include <windows.h>
#include <iostream>
#include <vector>
#include <string>

#include <pybind11/pybind11.h> ////
#include <pybind11/stl.h>      ////必须包含这个以支持 STL 容器
namespace py = pybind11;       ////

// 定义 MySQL 基本类型
struct st_mysql;
struct st_mysql_res;

// 定义 MYSQL 类型别名
typedef struct st_mysql MYSQL;
typedef struct st_mysql_res MYSQL_RES;

// 定义 MYSQL_ROW 为 char** 类型
typedef char **MYSQL_ROW;

// 定义函数指针类型
typedef MYSQL *(*mysql_init_t)(MYSQL *);
typedef MYSQL *(*mysql_real_connect_t)(MYSQL *, const char *, const char *, const char *, const char *, unsigned int, const char *, unsigned long);
typedef int (*mysql_query_t)(MYSQL *, const char *);
typedef MYSQL_RES *(*mysql_store_result_t)(MYSQL *);
typedef MYSQL_ROW (*mysql_fetch_row_t)(MYSQL_RES *);
typedef unsigned int (*mysql_num_fields_t)(MYSQL_RES *);
typedef void (*mysql_free_result_t)(MYSQL_RES *);
typedef void (*mysql_close_t)(MYSQL *);
typedef const char *(*mysql_error_t)(MYSQL *);

// 函数1
int add(int a, int b) { return a + b; }

// 函数2
std::string greet(const std::string &name)
{
    return "Hello, " + name + "!" + "你不fdg 行！ ";
}

// 类2: 字符串工具
class StringUtils
{
public:
    static std::string reverse(const std::string &s)
    {
        return std::string(s.rbegin(), s.rend());
    }
};

///////////////////////////////////////////////////////////////////

class MySQLWrapper
{
private:
    HMODULE hLib;
    MYSQL *mysql;

    // 函数指针
    mysql_init_t p_mysql_init;
    mysql_real_connect_t p_mysql_real_connect;
    mysql_query_t p_mysql_query;
    mysql_store_result_t p_mysql_store_result;
    mysql_fetch_row_t p_mysql_fetch_row;
    mysql_num_fields_t p_mysql_num_fields;
    mysql_free_result_t p_mysql_free_result;
    mysql_close_t p_mysql_close;
    mysql_error_t p_mysql_error;

public:
    MySQLWrapper() : hLib(NULL), mysql(NULL)
    {
        // 加载 libmysql.dll
        hLib = LoadLibraryA("libmysql.dll");
        if (!hLib)
        {
            std::cerr << "无法加载 libmysql.dll" << std::endl;
            return;
        }

        // 获取函数地址
        p_mysql_init = (mysql_init_t)GetProcAddress(hLib, "mysql_init");
        p_mysql_real_connect = (mysql_real_connect_t)GetProcAddress(hLib, "mysql_real_connect");
        p_mysql_query = (mysql_query_t)GetProcAddress(hLib, "mysql_query");
        p_mysql_store_result = (mysql_store_result_t)GetProcAddress(hLib, "mysql_store_result");
        p_mysql_fetch_row = (mysql_fetch_row_t)GetProcAddress(hLib, "mysql_fetch_row");
        p_mysql_num_fields = (mysql_num_fields_t)GetProcAddress(hLib, "mysql_num_fields");
        p_mysql_free_result = (mysql_free_result_t)GetProcAddress(hLib, "mysql_free_result");
        p_mysql_close = (mysql_close_t)GetProcAddress(hLib, "mysql_close");
        p_mysql_error = (mysql_error_t)GetProcAddress(hLib, "mysql_error");

        if (!p_mysql_init || !p_mysql_real_connect || !p_mysql_query || !p_mysql_store_result ||
            !p_mysql_fetch_row || !p_mysql_num_fields || !p_mysql_free_result || !p_mysql_close || !p_mysql_error)
        {
            std::cerr << "无法获取 MySQL 函数指针" << std::endl;
            FreeLibrary(hLib);
            hLib = NULL;
            return;
        }

        // 初始化 MySQL 连接
        mysql = p_mysql_init(NULL);
        if (!mysql)
        {
            std::cerr << "mysql_init() 失败" << std::endl;
            return;
        }
    }

    ~MySQLWrapper()
    {
        if (mysql)
        {
            p_mysql_close(mysql);
        }
        if (hLib)
        {
            FreeLibrary(hLib);
        }
    }

    bool connect(const char *host, const char *user, const char *passwd, const char *db, unsigned int port = 3306)
    {
        if (!mysql)
            return false;

        MYSQL *conn = p_mysql_real_connect(mysql, host, user, passwd, db, port, NULL, 0);
        if (!conn)
        {
            std::cerr << "连接失败: " << p_mysql_error(mysql) << std::endl;
            return false;
        }
        return true;
    }

    bool query(const char *sql)
    {
        if (!mysql)
            return false;

        if (p_mysql_query(mysql, sql))
        {
            std::cerr << "查询失败: " << p_mysql_error(mysql) << std::endl;
            return false;
        }
        return true;
    }

    // std::vector<std::vector<std::string>> fetch_results()
    std::vector<std::vector<std::string>> fetch_results()
    {
        std::vector<std::vector<std::string>> results;
        if (!mysql)
            return results;

        MYSQL_RES *res = p_mysql_store_result(mysql);
        if (!res)
        {
            // 可能是没有结果的查询 (如 INSERT, UPDATE 等)
            return results;
        }

        unsigned int num_fields = p_mysql_num_fields(res);
        MYSQL_ROW row;

        while ((row = p_mysql_fetch_row(res)))
        {
            std::vector<std::string> row_data;
            for (unsigned int i = 0; i < num_fields; i++)
            {
                row_data.push_back(row[i] ? row[i] : "NULL");
            }
            results.push_back(row_data);
        }

        p_mysql_free_result(res);
        return results;
    }

    void printResults(const std::vector<std::vector<std::string>> &results)
    {
        for (const auto &row : results)
        {
            for (const auto &field : row)
            {
                std::cout << field << "\t";
            }
            std::cout << std::endl;
        }
    }
};

PYBIND11_MODULE(example, m) ////
{
    m.def("add", &add, "Add two integers");
    m.def("greet", &greet, "Generate a greeting");

    //////////////////////////////////////////////////////////////////////
    // 暴露StringUtils类
    py::class_<StringUtils>(m, "StringUtils")
        .def_static("reverse", &StringUtils::reverse);

    py::class_<MySQLWrapper>(m, "MySQL")                     ////
        .def(py::init<>())                                   ////
        .def("connect", &MySQLWrapper::connect,              ////
             py::arg("host"), py::arg("user"),               ////
             py::arg("password"), py::arg("database"),       ////
             py::arg("port") = 3306)                         ////
        .def("query", &MySQLWrapper::query)                  ////
        .def("fetch_results", &MySQLWrapper::fetch_results); ////

    //////////////////////////////////////////////////////////////////////创建子模块 'math'
    auto math = m.def_submodule("math");
    math.def("add", [](int a, int b)
             { return a + b; });
    math.def("mul", [](int a, int b)
             { return a * b; });

    // 创建子模块 'str'
    auto str = m.def_submodule("str");
    str.def("uppercase", [](const std::string &s)
            {
        std::string result = s;
        std::transform(result.begin(), result.end(), result.begin(), ::toupper);
        return result; });
} ////

// int main()
// {
//     MySQLWrapper mysql;

//     // 连接数据库 (修改为你的数据库信息)
//     if (!mysql.connect("localhost", "root", "zst654321", "mysql"))
//     {
//         return 1;
//     }

//     // 创建表
//     mysql.query("DROP TABLE IF EXISTS users");
//     mysql.query("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT)");

//     // 插入数据
//     mysql.query("INSERT INTO users (name, age) VALUES ('Alice', 25)");
//     mysql.query("INSERT INTO users (name, age) VALUES ('Bob', 30)");
//     mysql.query("INSERT INTO users (name, age) VALUES ('Charlie', 35)");

//     // 查询数据
//     std::cout << "插入后的数据:" << std::endl;
//     mysql.query("SELECT * FROM users");
//     auto results = mysql.fetch_results();
//     mysql.printResults(results);

//     // 更新数据
//     mysql.query("UPDATE users SET age = 26 WHERE name = 'Alice'");

//     std::cout << "\n更新后的数据:" << std::endl;
//     mysql.query("SELECT * FROM users");
//     results = mysql.fetch_results();
//     mysql.printResults(results);

//     // 删除数据
//     mysql.query("DELETE FROM users WHERE name = 'Bob'");

//     std::cout << "\n删除后的数据:" << std::endl;
//     mysql.query("SELECT * FROM users");
//     results = mysql.fetch_results();
//     mysql.printResults(results);

//     return 0;
// }
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
