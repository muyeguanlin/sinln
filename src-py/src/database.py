import MySQLdb
# from contextlib import closing
import sys
import logging
import tomllib


class DatabaseManager:
    def __init__(self):
        with open('mysql.toml', 'rb') as mysql:
            toml = tomllib.load(mysql)  # config 是一个字典
        # toml = tomllib.load('mysql.toml')
        self.db_config = toml['database']
        self.sql_commands = toml['query']
        # self.logger = logging.getLogger(__name__)s
        print(self.sql_commands)
        
  
    def fix_and_insert_user(self,image_data):
        # print(sys.path) #模块搜索路径列表
        
        try:
            with MySQLdb.connect(**self.db_config) as db:

                print("数据库连接成功")            
                cursor = db.cursor()
                insert_sql =self.sql_commands['insert_image']
                # insert_sql= self.sql_commands.get('insert_image')

                # insert_sql = """
                # INSERT INTO baidu_images (image_name, image_url, keyword, local_path) 
                # VALUES (%s, %s, %s, %s)
                # ON DUPLICATE KEY UPDATE 
                #     image_url = VALUES(image_url),
                #     keyword = VALUES(keyword),
                #     local_path = VALUES(local_path),
                #     download_time = CURRENT_TIMESTAMP
                # """
           
        
   
     
                cursor.executemany(insert_sql, image_data)
                # cursor.execute(self.sql_commands['delete_all'])
                cursor.execute(self.sql_commands['select_all'])
            
            
                # 获取结果
                results = cursor.fetchall()
                print("查询结果:")
                for row in results:
                    print(row)

                db.commit()
                print(f"批量保存成功，共 {len(image_data)} 条记录")
            
                return True
        





                
             ##  
                # # 3. 现在可以安全插入数据
                # cursor.execute("select name from baidu_images")
                # namelist = [coll[0] for coll in cursor.fetchall()]
                # print(namelist) 
            
                # if '张三'  not in namelist:

                #     insert_sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
                #     user_data = ("张三", "zhangsan@example.com", 25)
                    
                #     cursor.execute(insert_sql, user_data)
                #     cursor.execute("select * from users")
                
                
                #     # 获取结果
                #     results = cursor.fetchall()
                #     print("查询结果:")
                #     for row in results:
                #         print(row)
    
                #     db.commit()
                #     print("数据插入成功!")
              
                
                # print("用户数据修复和插入完成")
                
        except MySQLdb.Error as e:
            print(f"数据库操作失败: {e}")
            return False
        except Exception as e:
            print(f"发生错误: {e}")
            return False
        return True
    
    # 可以添加其他数据库操作方法
    def execute_query(self, query, params=None):
        """执行查询"""
        try:
          
            with MySQLdb.connect(**self.db_config) as db:
                cursor = db.cursor()
                cursor.execute(query, params or ())
                return cursor.fetchall()
        except MySQLdb.Error as e:
            print(f"查询执行失败: {e}")
            return None
        


            
       
        


if  __name__=='__main__':
    # 配置和使用
    # db_config = {
    #     'host': 'localhost',
    #     'user': 'root',
    #     'passwd': 'zst654321',
    #     'db': 'mysql',
    #     'port': 3306,
    #     'charset': 'utf8',
    #     'autocommit': True
    # }

    # 创建实例并调用方法
    dd = DatabaseManager()

    data=[('诗经_6.jpg', 'https://img0.baidu.com/it/u=639488709,1180855375&fm=253&fmt=auto&app=120&f=JPEG?w=859&h=500', '诗经002', 'images/诗经_001.jpg'),
          ('诗经_7.jpg', 'https://img0.baidu.com/it/u=1961537966,854608005&fm=253&app=138&f=JPEG?w=500&h=653', '诗经003','images/诗经_004.jpg')]
    success = dd.fix_and_insert_user(data)

    if success:
        print("操作成功完成")
    else:
        print("操作失败")
