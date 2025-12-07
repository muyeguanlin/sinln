import MySQLdb  # 注意：这里导入的是MySQLdb，不是pymysql
import os

# ===== 配置区（请根据实际情况修改）=====
db_config = {
    'host': 'localhost',      # 数据库地址
    'port': 3306,            # 端口，默认3306
    'user': 'root',          # 用户名
    'password': 'zst654321',  # 密码
    'db': 'mysql', # 要连接的数据库名（确保已存在）
    'charset': 'utf8mb4'     # 字符集
}

sql_file_path = './resource/en_words.sql'  # SQL文件路径
# =======================================

def execute_sql_file():
    connection = None
    cursor = None
    
    try:
        # 1. 读取SQL文件内容
        with open(sql_file_path, 'r', encoding='utf-8') as file:
            sql_content = file.read()
        
        print(f"已成功读取SQL文件: {sql_file_path}")
        
        # 2. 连接MySQL数据库 (关键修正点1)
        print("正在连接MySQL数据库...")
        connection = MySQLdb.connect(**db_config)  # 直接调用 connect()
        cursor = connection.cursor()
        print("数据库连接成功!")
        
        # 3. 执行SQL语句 (建议使用分号分割)
        print("开始执行SQL语句...")
        
        sql_statements = sql_content.split(';')
        for statement in sql_statements:
            if statement.strip():  # 跳过空语句
                cursor.execute(statement)
        
        # 4. 提交事务
        connection.commit()
        print("SQL文件执行成功！数据已提交到数据库。")
        
    except FileNotFoundError:
        print(f"错误：找不到SQL文件 '{sql_file_path}'")
        print(f"当前工作目录: {os.getcwd()}")
        
    # 关键修正点2：捕获MySQLdb的错误
    except MySQLdb.OperationalError as e:
        print(f"数据库连接错误: {e}")
        if connection:
            connection.rollback()
    except MySQLdb.Error as e:  # 也可以捕获更通用的错误
        print(f"MySQL数据库错误: {e}")
        if connection:
            connection.rollback()
    except Exception as e:
        print(f"执行过程中出现错误: {e}")
        if connection:
            connection.rollback()
            print("已执行回滚操作，数据变更已撤销。")
            
    finally:
        # 5. 关闭连接
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("数据库连接已关闭。")

if __name__ == "__main__":
    execute_sql_file()