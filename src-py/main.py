
#######   打开web view外壳




# import webview
# import threading
# from src.server import WebAppServer

# def run_server():
#     """在单独线程中运行服务器"""
#     basedir = r'F:\study251011\sinln\dist'  # 您的dist文件夹路径
#     server = WebAppServer(basedir)
#     server.run()

# if __name__ == '__main__':
#     # Start the server in a separate thread
#     server_thread = threading.Thread(target=run_server)
#     server_thread.daemon = True
#     server_thread.start()
    
#     # Create webview window
#     window = webview.create_window(
#         'Arco Design Pro', 
#         'http:#localhost:1420',
#         width=1200,
#         height=800,
#         resizable=True,
#         text_select=True
#     )
    
#     webview.start()
##########################################################################################


# # nodemon --config package.json       # 用nodemon实现热启动
#   "exec": "cmd /c build.bat && python main.py", #nodemon 命令

#######################################################################################
#########       调用Op.dll


# from win32com.client import Dispatch
# class Demo:
#     def __init__(self):
#         #创建com对象
#         self.op=op=Dispatch("op.opsoft");
#         self.hwnd=66892;
#         self.send_hwnd=0;
#         # print("init");


#     def test_base(self):
#          #输出插件版本号
#          print("op ver:",self.op.Ver());
#          print("path:",self.op.GetPath());
#          self.op.SetShowErrorMsg(2);
#          r=self.op.WinExec("notepad",1);
#          print("Exec notepad:",r);



#     def test_window_api(self):
#         #测试窗口接口

#         self.hwnd = self.op.FindWindow("","PdfView");
#         print("parent hwnd:",self.hwnd);
#         if self.hwnd:
#             self.send_hwnd=self.op.FindWindowEx(self.hwnd,"Edit","");
#         print("child hwnd:",self.send_hwnd);
#         return 0;

#     def test_bkmode(self):
#         r=self.op.BindWindow(self.hwnd,"gdi","normal","normal",0);
#         if r == 0:
#             print("bind false");
#         return r;

#     def test_bkmouse_bkkeypad(self):
#         self.op.MoveTo(200,200);
#         self.op.Sleep(200);
#         self.op.LeftClick();
#         self.op.Sleep(1000);
#         r=self.op.SendString(self.send_hwnd,"Hello World!");
#         print("SendString ret:",r);
#         self.op.Sleep(1000);
#         return 0;

#     def test_bkimage(self):
#         cr=self.op.GetColor(30,30);
#         print("color of (30,30):",cr);
#         ret=self.op.Capture(0,0,2000,2000,"screen.bmp");
#         print("op.Capture ret:",ret);
#         r,x,y=self.op.FindPic(0,0,100,100,"test.png","000000",1.0,0);
#         print("op.FindPic:",r,x,y);
#         return 0;

#     def test_ocr(self):
#         s=self.op.OcrAuto(0,0,100,100,0.9);
#         print("ocr:",s);
#         s=self.op.OcrEx(0,0,100,100,"000000-020202",0.9);
#         print("OcrEx:",s);
#         s=self.op.OcrAutoFromFile("screen.bmp",0.95);
#         print("OcrAutoFromFile:",s);
#         return 0;
#     def test_clear(self):
#         self.op.UnBindWindow();


# def test_all():
#     demo=Demo();
#     demo.test_base();
#     demo.test_window_api();
#     if demo.test_bkmode() == 0:
#         return 0;
#     demo.test_bkmouse_bkkeypad();
#     demo.test_bkimage();
#     demo.test_ocr();
#     demo.test_clear();

#     return 0;

# #run all test

# test_all();



#######################################################################################
######### playwright 爬取百度图片


# import os
# import aiohttp
# import asyncio
# from playwright.async_api import async_playwright



# # async def download_single_image(session, url, index):
# #     """异步下载单张图片"""
# #     try:
# #         async with session.get(url) as response:
# #             if response.status == 200:
# #                 content = await response.read()
# #                 with open(f"flowers/flower_{index+1}.jpg", "wb") as f:
# #                     f.write(content)
# #                 print(f"下载成功：flower_{index+1}.jpg")
# #     except Exception as e:
# #         print(f"下载失败 {url}: {e}")


# async def download_images(max_images=100):
#     """
#     异步下载图片
#     :param max_images: 要下载的数量，默认100张
#     """
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         # browser = await p.chromium.launch(headless=True)
#         page = await browser.new_page()
#         await page.goto("https:#www.pexels.com/zh-cn/search/鲜花/",timeout=60000)
        
#         # 接受 Cookie
#         if await page.query_selector("button:has-text('接受所有')"):
#             await page.click("button:has-text('接受所有')")
        
#         # 等待图片加载
#         await page.wait_for_selector("img[src]", timeout=160000)
#         img_elements = await page.query_selector_all("img[src]")

#         if img_elements:
#             print("悬浮在第一张图片上...")
#             await img_elements[0].hover()  # 悬停触发下载按钮
        
#         await page.wait_for_selector("a[download]")
#         img_urls = set()  # 使用集合去重

#         scroll_pause_time = 2  # 滚动等待时间
        
#         while len(img_urls) < max_images:
#             a_elements = await page.query_selector_all("a[download]")
#             for img in a_elements:
#                 url = await img.get_attribute("href")
#                 if url and url.startswith("https"):
#                     img_urls.add(url)

#             print(f"已获取 {len(img_urls)} 张图片")
#             await page.mouse.wheel(0, 1000)  # 异步滚动
#             await asyncio.sleep(scroll_pause_time)  # 异步等待
        
#         # 创建目录
#         os.makedirs("flowers", exist_ok=True)

#         # 异步下载图片
#         async with aiohttp.ClientSession() as session:
#             # tasks = []
#             for i, url in enumerate(list(img_urls)[:max_images]):


#                 # tasks.append(download_single_image(session, url, i))
#                 async with session.get(url) as response:
#                     if response.status == 200:
#                         content = await response.read()
#                         with open(f"flowers/flower_{i+1}.jpg", "wb") as f:
#                             f.write(content)
#                         print(f"下载成功：flower_{i+1}.jpg")
            
#             # await asyncio.gather(*tasks)  # 并发下载

#         await browser.close()


# if __name__ == "__main__":
#     asyncio.run(download_images(10))


# # #################################################################################
# # #### libmysql.dll  pybind11



# import sys
# import os
# import modules


# # # 获取当前脚本所在目录
# # script_dir = os.path.dirname(os.path.abspath(__file__))

# # # 构建 `build/debug` 的相对路径（假设脚本在项目根目录）
# # build_debug_dir = os.path.join(script_dir, "build", "debug")

# # # 添加到 Python 模块搜索路径
# # sys.path.append(build_debug_dir)

# import example # type: ignore

# db = example.MySQL()

# # 连接数据库
# db.connect("localhost", "root", "zst654321", "mysql")

# # 创建表
# db.query("DROP TABLE IF EXISTS users")
# db.query("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT)")

# # 插入数据
# db.query("INSERT INTO users (name, age) VALUES ('Alice', 25)")
# db.query("INSERT INTO users (name, age) VALUES ('Bob', 30)")

# # # 查询数据
# db.query("SELECT * FROM users")
# results = db.fetch_results()
# print("查询结果:")
# for row in results:
#     print(row)

# # 更新数据
# db.query("UPDATE users SET age = 26 WHERE name = 'Alice'")

# # # 再次查询
# db.query("SELECT * FROM users")
# print("\n更新后的结果:")
# for row in db.fetch_results():
#     print(row)

# # 删除数据
# db.query("DELETE FROM users WHERE name = 'Bob'")

# # 最终查询
# db.query("SELECT * FROM users")
# print("\n删除后的结果:")
# for row in db.fetch_results():
#     print(row)

# # from example import MathUtils, StringUtils# type: ignore #引入类

# print(example.add(2, 3))      # 输出: 5
# print(example.greet("Alice")) # 输出: Hello, Alice!

# # print(example.MathUtils.square(4))       # 输出: 16
# print(example.StringUtils.reverse("abc")) # 输出: cba

# print(example.math.add(2, 3))          # 输出: 5
# print(example.str.uppercase("hello"))  # 输出: HELLO



# url = "mysql:#root:zst654321@localhost:3306/mysql"
# # print(modules.sum_as_string(15, 10))  # 输出 "15"
# version = modules.get_mysql_version(url)
# print(f"MySQL Version: {version}")

# # 测试执行查询
# results = modules.execute_query(url, "SELECT * FROM db")
# for row in results:
#     print(row)
##################################################################################################################
######   fastapi后端

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
#########################################################
# # ###用python调用mysql
# import pymysql
# from pymysql import Error

# try:
#     # 创建数据库连接
#     connection = pymysql.connect(
#         host='localhost',
#         # port='3306',
#         user='root',
#         password='zst654321',
#         database='mysql',
#         charset='utf8mb4',
#         cursorclass=pymysql.cursors.DictCursor  # 返回字典形式的结果
#     )
    
#     print("成功连接到 MySQL 数据库")
    
#     with connection.cursor() as cursor:
#         # 执行SQL查询
#         sql = "SELECT * FROM db LIMIT 5"
#         cursor.execute(sql)
        
#         # 获取结果
#         results = cursor.fetchall()
#         print("查询结果:")
#         for row in results:
#             print(row)
            
#     # 提交事务
#     connection.commit()
    
# except Error as e:
#     print(f"连接或查询过程中发生错误: {e}")
    
# finally:
#     # 关闭连接
#     if 'connection' in locals() and connection.open:
#         connection.close()
#         print("MySQL 连接已关闭")
################################################################################
# ####mysqlclient


# import MySQLdb
# from contextlib import closing
# import sys


# class dbexe:
#     def fix_and_insert_user(self):
#         print(sys.path)

#         # db = None #如果连接成功，db 是有效的连接对象，可以调用 close()。

#     #如果连接失败（例如密码错误），db 仍然是 None，此时 if db: 会跳过关闭操作，避免对 None 调用方法导致异常。


#         try:
#             # 连接数据库
#             # db = MySQLdb.connect(
#             #     host="localhost",
#             #     user="root",
#             #     passwd="zst654321",
#             #     db="mysql",
#             #     charset="utf8",
#             #     autocommit=True  ##自动提交
#             # )
#             with closing(MySQLdb.connect(#：将不支持 with 的对象（如 MySQLdb 连接）变成支持自动资源管理的对象。
#                 host="localhost",
#                 user="root",
#                 passwd="zst654321",
#                 db="mysql",
#                 charset="utf8",
#                 autocommit=True  ##自动提交
#             )) as db:  # 自动关闭连接
#                 cursor = db.cursor()#创建游标对象，执行sql语句
                
#                 # 1. 检查表结构
#                 cursor.execute("DESCRIBE users")
#                 columns = [col[0] for col in cursor.fetchall()]
#                 print("当前列:", columns)
                
#                 # 2. 如果缺少email列则添加
#                 if 'email' not in columns:
#                     print("检测到缺少email列，正在添加...")
#                     cursor.execute("ALTER TABLE users ADD COLUMN email VARCHAR(100) AFTER name")
#                     db.commit()
#                     print("成功添加email列")             
                
#                 # 3. 现在可以安全插入数据
#                 cursor.execute("select name from users")
#                 namelist = [coll[0] for coll in cursor.fetchall()]
#                 print(namelist) 
            
#                 if '张三'  not in namelist:

#                     insert_sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
#                     user_data = ("张三", "zhangsan@example.com", 25)
                    
#                     cursor.execute(insert_sql, user_data)
#                     cursor.execute("select * from users")
                
                
#                     # 获取结果
#                     results = cursor.fetchall()
#                     print("查询结果:")
#                     for row in results:
#                         print(row)
    
#                     db.commit()
#                     print("数据插入成功!")
            
#         # except MySQLdb.Error as e:
#         except Exception as e:
#             print(f"数据库错误: {e}")
#             if db: db.rollback()#如果 db 有效，则执行回滚操作，撤销当前事务中的所有未提交更改（恢复到事务开始前的状态）。
#         # finally:
#         #     if db: db.close()

#     # 执行修复和插入
# dd=dbexe()
# dd.fix_and_insert_user()
# ################################################################################
# ###yolo挂机
# import cv2
# import numpy as np
# from ultralytics import YOLO
# # import pydirectinput as pdi #使用pydirectinput代替pyautogui （更接近真实输入）
# import pyautogui
# import mss
# import time
# import random

# # 加载 YOLO 模型（可以是自定义训练的）
# model = YOLO("./yolo11n.pt")  # 或 yolov8s.pt, yolov8m.pt 等   加载预训练模型
# # model.train(data="custom_data.yaml", epochs=50)  # 训练

# # 设置屏幕捕获区域（全屏或指定区域）
# monitor = {"top": 0, "left": 3843, "width": 1280, "height":720}  # 根据你的分辨率调


# last_detection_time = 0
# detection_interval = 1.0  # 1秒检测一次
# total_detections = 0  # 必须先定义并初始化这个计数器
# with mss.mss() as sct:
#     while True:
        
#         # 捕获屏幕
#         screenshot = np.array(sct.grab(monitor))
#         frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)  # MSS 返回 BGRA，转 BGR

#         # YOLO 检测 每隔 N 秒检测一次，避免高频检测
#         current_time = time.time()
#         if current_time - last_detection_time >= detection_interval:
#             results = model(frame)
#             last_detection_time = current_time  # 更新检测时间      
#             detections = results[0].boxes.data.tolist()  # 获取检测结果 [x1, y1, x2, y2, conf, cls]
#              # 更新总检测次数
#             total_detections += len(detections)
# w 
#         # 遍历检测到的目标
#         for det in detections:
#             x1, y1, x2, y2, conf, cls_id = det
#             if conf > 0.4:  # 置信度阈值

#                 pyautogui.press('F1')  # 按下并释放
               

#                 label = model.names[int(cls_id)]  # 类别名称
#                 print(f"Detected: {label} at ({x1}, {y1})")

#                 # 计算目标中心点（用于点击）
#                 center_x = (x1 + x2) # 2
#                 center_y = (y1 + y2) # 2

#                 # 4. 模拟鼠标点击（攻击敌人）
              
#                 pyautogui.moveTo(center_x, center_y)  # 移动鼠标
#                 pyautogui.middleClick()  # 在当前鼠标位置中键点击
#                 pyautogui.keyDown('w')
#                 time.sleep(0.3)
#                 # pyautogui.moveRel(100, 0, duration=0.001)  # duration参数控制移动速度（秒） 
#                 pyautogui.keyUp('w')

                
#                 # # 方法2：移动到指定位置后右键点击
#                 # pyautogui.rightClick(x=100, y=200)  # 在坐标(100,200)处右键点击
#                 if total_detections % 5 ==0:
#                     pyautogui.rightClick()  # 在当前鼠标位置右键点击
#                 elif total_detections % 5 ==1:
#                     pyautogui.press('q')  # 按下并释放
#                 elif total_detections % 5 ==2:
#                     pyautogui.press('F2')  # 按下并释放
#                     pyautogui.press('e')  # 按下并释放
#                 elif total_detections % 5 ==3:
#                     pyautogui.press('r')  # 按下并释放
#                 else:
#                     pyautogui.press('space')  # 按下并释放
                
        

#                 pyautogui.click()  # 左键点击
#                 # pdi.moveTo(center_x, center_y, duration=0.2)  # 模拟人类移动速度
#                 # pdi.click()
#                 print(f"攻击敌人坐标: ({center_x}, {center_y})")
#                 # time.sleep(0.1)  # 攻击间隔（避免过快操作）
#                 # time.sleep(random.uniform(0.1, 0.5))  # 随机延迟
#             else:
#                 pyautogui.keyDown('s')
#                 time.sleep(0.5)
#                 # pyautogui.moveRel(100, 0, duration=0.001)  # duration参数控制移动速度（秒） 
#                 pyautogui.keyUp('s')
                

#         # 显示检测结果（可选）
#         annotated_frame = results[0].plot()
#         cv2.imshow("YOLO Game Bot", annotated_frame)

#         # 按 'q' 退出
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break

# cv2.destroyAllWindows()

#####################################################################################
# from win32com.client import Dispatch
# import time

# op=Dispatch("op.opsoft")

# time.sleep(2.5)
# hwnd = op.GetMousePointWindow()  #获取鼠标指向的窗口句柄
# print(hwnd)
# op_ret = op.BindWindow(hwnd,"gdi","normal","normal",0)
# print(op_ret)


# for i in range(1000):
#     op.KeyPress(87) #w
#     time.sleep(0.05)

#     op.KeyPress(68) #d
#     time.sleep(0.05)

#     op.KeyPress(83) #s
#     time.sleep(0.05)

#     op.KeyPress(65) #a
#     time.sleep(0.05)



#####################################################################################   
# from win32com.client import Dispatch
# import time
# import random
# import os

# # import ctypes
# # WndEx= ctypes.CDLL('./WndEx7_71.dll')  # Windows用'sine.dll'，Linux/Mac用'./libsine.so'
# # mysql= ctypes.CDLL('.libmysql.dll')  # Windows用'sine.dll'，Linux/Mac用'./libsine.so'

# # WndEx.SetFakeActive.argtypes = [ctypes.c_long,ctypes.c_long]  # 参数类型
# # WndEx.SetFakeActive.restype = None            # 返回类型

# # # 调用函数
# # WndEx.SetFakeActive(ctypes.c_long(hwnd), ctypes.c_long(a))

# op=Dispatch("op.opsoft")
# print(op.Ver())
# ##create op instance 创建op对象

# # dm=Dispatch("dm.dmsoft")
# # print(dm.Ver())

# # ts=Dispatch("ts.tssoft")
# # print(ts.Ver()+"hello")
# time.sleep(3)
# path=op.AStarFindPath(1908,339,"1,0|1,1|1,2|1,3",0,0,3340,891)
# print(path)
# # base_path = op.GetBasePath()
# # print(base_path)

# hwnd = op.FindWindow("","Bless Unleashed") 
# print(hwnd)
# op_ret = op.BindWindow(hwnd,"gdi","windows","windows",1)
# time.sleep(2)
# for i in range(10):
#     op.KeyDown(87)
#     time.sleep(2)
#     op.KeyUp(87)

#     op.KeyDown(68)
#     time.sleep(2)
#     op.KeyUp(68)

#     op.KeyDown(83)
#     time.sleep(2)
#     op.KeyUp(83)

#     op.KeyDown(65)
#     time.sleep(2)
#     op.KeyUp(65)


# print(op_ret)
# # # 查找游戏窗口（根据标题关键字）
# time.sleep(3)
# hwnd = dm.FindWindow("", "Bless Unleashed")  # 替换为你的游戏窗口标题
# print(hwnd)
# if not hwnd:
#     print("未找到窗口！")
#     exit()
# dm_ret1 = dm.BindWindowEx(hwnd,"dx3","dx.mouse.position.lock.api|dx.mouse.position.lock.message","windows","dx.public.active.api",0)

# for i in range(20):
   
#     dm.LeftClick
#     dm_ret = dm.KeyDown(87)
#     time.sleep(2)
#     dm_ret = dm.KeyUp(87)

#     dm.LeftClick
#     dm_ret = dm.KeyDown(68)
#     time.sleep(2)
#     dm_ret = dm.KeyUp(68)

#     dm.LeftClick
#     dm_ret = dm.KeyDown(83)
#     time.sleep(2)
#     dm_ret = dm.KeyUp(83)

#     dm.LeftClick
#     dm_ret = dm.KeyDown(65)
#     time.sleep(2)
#     dm_ret = dm.KeyUp(65)


#####################################################################################   
# ###使用zipfile模块进行字典攻击（ZIP文件） 多线程
# import zipfile
# import itertools
# from concurrent.futures import ThreadPoolExecutor

# def try_password(zip_file, password):
#     try:
#         zip_file.extractall(pwd=password.encode())
#         return password
#     except:
#         return None

# def crack_zip_parallel(zip_path, charset, max_length=4, workers=4):
#     zf = zipfile.ZipFile(zip_path)
    
#     with ThreadPoolExecutor(max_workers=workers) as executor:
#         for length in range(1, max_length + 1):
#             for attempt in itertools.product(charset, repeat=length):
#                 password = ''.join(attempt)
#                 print(password)
#                 future = executor.submit(try_password, zf, password)
#                 if future.result():
#                     print(f"成功! 密码是: {password}")
#                     return password
    
#     print("破解失败!")
#     return None
# if __name__ == "__main__":
    # # 使用示例
    # crack_zip_parallel(r'C:\Users\Administrator\Desktop\《Python编程（第3版）：从入门到实践》\Python编程（第3版）：从入门到实践_ - 副本.zip', 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+<>?*')
##########################################################################################

# import os
# import requests
# from playwright.sync_api import sync_playwright
# import time
 
# def download_images(max_images=100):
    
#     """
#     max_images 要下载的数量，默认100张
#     """
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # 设为无头模式
#         page = browser.new_page()
#         page.goto("https:#www.pexels.com/zh-cn/search/鲜花/")
        
#         # 接受 Cookie
#         if page.query_selector("button:has-text('接受所有')"):
#             page.click("button:has-text('接受所有')")
        
#         # 等待图片加载
#         page.wait_for_selector("img[src]")
#         img_elements = page.query_selector_all("img[src]")
 
#         if img_elements:
#             print("悬浮在第一张图片上...")
#             img_elements[0].hover()  # 让鼠标悬停在第一张图片上使得<a download="" >标签可以显示出来
#         # 等待图片加载


#         page.wait_for_selector("a[download]")       
#         img_urls = set()  # 使用集合防止重复 
#         scroll_pause_time = 2  # 每次滚动后等待时间        
#         while len(img_urls) < max_images:
#             # 获取当前页面上的图片链接
#             a_elements = page.query_selector_all("a[download]")
#             for img in a_elements:
#                 url = img.get_attribute("href")
#                 if url and url.startswith("https"):
#                     img_urls.add(url)
 
#             print(f"已获取 {len(img_urls)} 张图片")
 
#             # 模拟滚动鼠标（向下滚 1000 像素）
#             page.mouse.wheel(0,1000)
#             time.sleep(scroll_pause_time)
            
        
#         # 创建存储目录
#         os.makedirs("flowers", exist_ok=True)
        
#         for i, url in enumerate(list(img_urls)[:max_images]):
#             response = requests.get(url)
#             with open(f"flowers/flower_{i+1}.jpg", "wb") as f:
#                 f.write(response.content)
#             print(f"下载成功：flower_{i+1}.jpg")
        
#         browser.close()
 
# download_images(100)

########################################################################################################################
# ####playwright 爬虫
# import os
# import aiohttp
# import asyncio
# from urllib import parse #用perse.quote 方法必须引入
# from playwright.async_api import async_playwright



# class BaiduImageDownloader:
#     async def download_single_image(self,session, url, index,word_origin ):
#         """异步下载单张图片"""
#         try:
#             async with session.get(url) as response:
#                 if response.status == 200:
#                     content = await response.read()
#                     with open(f"images/{word_origin}_{index+1}.jpg", "wb") as f:
#                         f.write(content)
#                     print(f"下载成功：{word_origin}_{index+1}.jpg")
#         except Exception as e:
#             print(f"下载失败 {url}: {e}")
        
        


#     async def download_images(self,max_images=100):
#         """
#         异步下载图片
#         :param max_images: 要下载的数量，默认100张
#         """
#         async with async_playwright() as p:
#             # browser = await p.chromium.launch(headless=False)
#             browser = await p.chromium.launch(headless=True)
#             # page = await browser.new_page()#简单场景

#             context = await browser.new_context()
#             page = await context.new_page()

#             # await page.goto("https:#www.pexels.com/zh-cn/search/鲜花/",timeout=60000)
#             word_origin = input("请输入搜索内容：")
#             # word = parse.quote(word_origin)
#             # http_url="https:#image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word="+word
#             # print(word)
#             # await page.goto(http_url,timeout=6000)

#             # 访问百度图片
#             await page.goto("https:#image.baidu.com/")
#             # await page.goto("https:#www.taobao.com/wow/z/tbhome/pcsem/alimama?refpid=mm_2898300158_3078300397_115665800437&keyword=%E6%B7%98%E5%AE%9D&bc_fl_src=tbsite_T9W2LtnM&channelSrp=bingSomama&msclkid=a4a83b81eb3210d11c9d53fb57b8ebc7&clk1=940a383ff07244828296edc9876d50ab&upsId=940a383ff07244828296edc9876d50ab")

#             print("已打开百度图片")

#             # 输入搜索关键词
#             # await page.fill("#image-search-input", word_origin)
#             await page.fill('input[name="word"]', word_origin)
#             # await page.fill('input[name="q"]', word_origin)
#             await page.press("#image-search-input", "Enter")
#             # await page.press('input[name="q"]', "Enter")
#             await page.wait_for_load_state("networkidle")
#             print("已提交搜索")

#             # 模拟滚动加载更多图片
#             for _ in range(5):  # 滚动5次加载更多内容
#                 await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#                 # await page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
#                 await page.wait_for_timeout(2000)  # 等待加载
#                 # await asyncio.sleep(2000)  # 异步等待


#             # 接受 Cookie
#             if await page.query_selector("button:has-text('接受所有')"): 
#                 await page.click("button:has-text('接受所有')")
            
#             # # 等待图片加载
#             await page.wait_for_selector("img[src]", timeout=6000)
#             # img_elements = await page.query_selector_all("img[src]")
#             img_elements = await page.locator("img[src]").all()  # 创建定位器 locator 对动态页面更棒：page.locator() 不需要 await，但加上.all（）就是异步的
#             # a_elements = await page.query_selector_all("img[src]")

#             # if img_elements:
#             #     print("悬浮在第一张图片上...")
#             #     await img_elements[0].hover()  # 悬停触发下载按钮
            
#             # await page.wait_for_selector("a[download]")

#             scroll_pause_time = 2  # 滚动等待时间
#             img_urls =set()  # 使用集合去重

#             while len(img_urls) < max_images:
#                 # a_elements = await page.query_selector_all("a[download]")
#                 # for img in a_elements:
#                 for img in img_elements:
#                     # url = await img.get_attribute("href")
#                     src = await img.get_attribute("src")         
#                     data_src = await img.get_attribute("data-src")
#                 # # 优先使用data-src（懒加载图片）
#                     url = data_src or src
#                     print(url)
#                     if url and url.startswith("http"):
#                         img_urls.add(url)
                    



#                 await page.mouse.wheel(0, 1000)  # 异步滚动
#                 await asyncio.sleep(scroll_pause_time)  # 异步等待
                            
#                 print(len(await page.query_selector_all("img[src]")))  # 检查实际有多少个 img 元素
#                 print(f"已获取 {len(img_urls)} 张图片")
    
            
#             # 创建目录
#             os.makedirs("images", exist_ok=True)

#             # 异步下载图片
#             async with aiohttp.ClientSession() as session:
#                 tasks = [self.download_single_image(session, url, i,word_origin) for i,url in enumerate(list(img_urls)[:max_images])]
#                 # tasks = []
#                 # for i, url in enumerate(list(img_urls)[:max_images]):
#                 #     tasks.append(download_single_image(session, url, i))
                
#                 await asyncio.gather(*tasks)  # 并发下载

#             await browser.close()
#             print(tasks)


# if __name__ == "__main__":
#     downloader=BaiduImageDownloader()
#     asyncio.run(downloader.download_images(80))



#         # db = MySQLdb.connect(
#                 #     host="localhost",
#                 #     user="root",
#                 #     passwd="zst654321",
#                 #     db="mysql",
#                 #     charset="utf8",
#                 #     autocommit=True  ##自动提交
#                 # )

#     ##############################################################################################################################


# download  --database.py
#########################################################################################
# pip install -r requirements.txt
# playwright install

import asyncio
import logging
# from mod.download import BaiduImageDownloader
# from mod.database import DatabaseManager

from src import BaiduImageDownloader,DatabaseManager

# import mod
# downloader = mod.BaiduImageDownloader()

# 配置日志




    
async def runxxxx(keywords: list, max_images_per_keyword: int):
    """运行下载程序"""
    try:
        # 连接数据库
       
        
        for word_origin in keywords:
            print(f"正在搜索和下载关键词: {word_origin}")
            
            # 下载图片
            downloaded_images = await downloader.download_images(
                word_origin, max_images_per_keyword
            )
            # print(downloaded_images)
            if downloaded_images:
                # 保存到数据库
                success = db_manager.fix_and_insert_user(downloaded_images)
                if success:
                    print(f"关键词 '{word_origin}' 处理完成，成功下载 {len(downloaded_images)} 张图片")
                else:
                    print(f"关键词 '{word_origin}' 图片下载成功但数据库保存失败")
            else:
                print(f"关键词 '{word_origin}' 未找到图片")
            
            # 短暂延迟，避免请求过于频繁
            await asyncio.sleep(2)

        
      
    except Exception as e:
        logging.error(f"程序运行出错: {e}")
    # finally:
    #     # 关闭数据库连接
    #     db_manager.close()


   

if __name__ == "__main__":
    

    downloader = BaiduImageDownloader()
    db_manager = DatabaseManager()


    # 搜索关键词列表
    searchword=input("请输入搜索关键字：")
    keywords = [searchword]
    
    # 创建应用实例并运行
  
    
    # 运行异步主程序
    asyncio.run(runxxxx(keywords, max_images_per_keyword=50))


#####################################################################################################
# import re
# import time

# text = "fasdasfHello" + " World" * 10  # 很长的字符串

# # 使用 re.match() - 只检查开头
# start = time.time()


# print( re.match(r"fasd", text))
# print( re.search(r"World", text))
# print( re.findall(r"World", text))

# it=re.finditer(r"World", text)
# print (next(it))
# # print (next(it))

# # print (next(it))
# # print (next(it))
# # print (next(it))

# # print (next(it))

# # print (next(it))
# # print (next(it))
# # print (next(it))

# # for x in it:
# #     print (x)

#####################################################################################################
# from win32com.client import Dispatch
# import time
# # op=Dispatch("op.opsoft");
# # #        
# # print(op.ver());
# ts=Dispatch("ts.tssoft");
# ts.ver()       
# print();
# hwnd=328276
# # 788984


# t=ts.SetFakeActive(hwnd)
# print(t);
# time.sleep(3)
# tb=ts.BindWindow(hwnd,"dx","dx","dx",1)
# print(tb);
# for _ in range(20):
#     a=[13,83,67,84,69,32,81]
#     ts.keydown(83)#S
#     ts.keydown(83)#S
#     ts.keydown(83)#S
#     time.sleep(0.3)
#     ts.keyup( 83)#S
#     for x in a:

#         tk=ts.KeyPress(x)
#         print(tk);
#         time.sleep(0.1)
