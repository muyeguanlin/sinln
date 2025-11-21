# import cv2
# import numpy as np
# import pyautogui
# import mss
# import time
# import keyboard
# import threading

# # 条件导入
# try:
#     from ultralytics import YOLO
#     YOLO_AVAILABLE = True
# except ImportError:
#     YOLO_AVAILABLE = False
#     print("警告: ultralytics 模块未安装")

# class YOLOPlugin:
#     _public_methods_ = ['start_detection', 'stop_detection', 'set_monitor_area', 'get_status']
#     _public_attrs_ = ['is_running', 'total_detections', 'exit_flag']
#     _reg_progid_ = "YOLOPlugin.GameAssistant"
#     _reg_clsid_ = "{12345678-1234-5678-1234-567812345678}"
    
#     def __init__(self):
#         self.model = None
#         self.monitor = {"top": 0, "left": 0, "width": 1280, "height": 720}
#         self.is_running = False
#         self.total_detections = 0
#         self.exit_flag = False
#         self.last_detection_time = 0
#         self.detection_interval = 1.0
        
#         pyautogui.FAILSAFE = True
#         pyautogui.PAUSE = 0.1
        
#         print("YOLO COM组件初始化完成")
    
#     def start_detection(self, model_path="./resource/yolo12n.pt"):
#         """开始检测"""
#         print(f"start_detection 方法被调用，模型路径: {model_path}")
        
#         if self.is_running:
#             return "检测已在运行中"
        
#         if not YOLO_AVAILABLE:
#             return "错误: ultralytics模块未安装"
        
#         # 加载模型
#         try:
#             print("正在加载YOLO模型...")
#             self.model = YOLO(model_path)
#             print("YOLO模型加载成功")
#         except Exception as e:
#             error_msg = f"模型加载失败: {e}"
#             print(error_msg)
#             return error_msg
        
#         self.is_running = True
#         self.exit_flag = False
#         self.total_detections = 0
        
#         # 启动检测线程
#         print("启动检测线程...")
#         self.detection_thread = threading.Thread(target=self._detection_loop)
#         self.detection_thread.daemon = True
#         self.detection_thread.start()
        
#         print("检测线程已启动")
#         return "YOLO检测已启动"
    
#     def stop_detection(self):
#         """停止检测"""
#         print("stop_detection 方法被调用")
        
#         if not self.is_running:
#             return "检测未在运行"
        
#         self.exit_flag = True
#         self.is_running = False
        
#         if hasattr(self, 'detection_thread') and self.detection_thread.is_alive():
#             self.detection_thread.join(timeout=3.0)
        
#         try:
#             keyboard.unhook_all()
#             cv2.destroyAllWindows()
#         except:
#             pass
        
#         return "YOLO检测已停止"
    
#     def set_monitor_area(self, top, left, width, height):
#         """设置监控区域"""
#         self.monitor = {"top": top, "left": left, "width": width, "height": height}
#         return f"监控区域已设置为: top={top}, left={left}, width={width}, height={height}"
    
#     def get_status(self):
#         """获取状态信息"""
#         status = {
#             "is_running": self.is_running,
#             "total_detections": self.total_detections,
#             "monitor_area": self.monitor,
#             "exit_flag": self.exit_flag,
#             "yolo_available": YOLO_AVAILABLE
#         }
#         return str(status)
    
#     def _detection_loop(self):
#         """检测循环"""
#         print("=" * 50)
#         print("YOLO挂机程序已启动!")
#         print("退出方式: 调用stop_detection()方法")
#         print("=" * 50)
        
#         def set_exit_flag():
#             print("\n检测到退出信号，正在安全退出...")
#             self.exit_flag = True
        
#         # 注册全局热键
#         keyboard.add_hotkey('esc', set_exit_flag)
#         keyboard.add_hotkey('f12', set_exit_flag)
        
#         try:
#             with mss.mss() as sct:
#                 print("mss截图工具初始化成功")
                
#                 while not self.exit_flag and self.is_running:
#                     print(f"开始第 {self.total_detections + 1} 次检测循环")
                    
#                     try:
#                         # 捕获屏幕
#                         screenshot = np.array(sct.grab(self.monitor))
#                         frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
#                         print("屏幕截图成功")
#                     except Exception as e:
#                         print(f"屏幕截图失败: {e}")
#                         time.sleep(1)
#                         continue
                    
#                     # YOLO 检测
#                     current_time = time.time()
#                     if current_time - self.last_detection_time >= self.detection_interval:
#                         try:
#                             print("开始YOLO检测...")
#                             results = self.model(frame)
#                             self.last_detection_time = current_time
#                             detections = results[0].boxes.data.tolist()
#                             self.total_detections += len(detections)
#                             print(f"检测到 {len(detections)} 个目标")
#                         except Exception as e:
#                             print(f"YOLO检测失败: {e}")
#                             detections = []
                    
#                     # 处理检测结果
#                     for det in detections:
#                         if self.exit_flag:
#                             break
                            
#                         x1, y1, x2, y2, conf, cls_id = det
#                         class_name = self.model.names[int(cls_id)]
                        
#                         if conf > 0.3 and class_name == "person":
#                             print(f"检测到人物，置信度: {conf:.2f}")
#                             # 这里添加你的游戏操作逻辑
#                             # pyautogui.press('3')
#                             # ... 其他操作
#                         else:
#                             print(f"检测到 {class_name}，置信度: {conf:.2f}，不满足条件")
                    
#                     # 显示检测结果
#                     try:
#                         if 'results' in locals() and results is not None:
#                             annotated_frame = results[0].plot()
#                             cv2.imshow("YOLO Game Bot", annotated_frame)
#                     except Exception as e:
#                         print(f"显示结果失败: {e}")
                    
#                     # 检查退出键
#                     if cv2.waitKey(1) & 0xFF == ord("q"):
#                         print("检测到OpenCV窗口退出信号")
#                         break
                    
#                     # 短暂延迟
#                     time.sleep(0.1)
                    
#         except Exception as e:
#             print(f"检测循环发生错误: {e}")
#         finally:
#             print("检测循环结束")
#             keyboard.unhook_all()
#             cv2.destroyAllWindows()
#             self.is_running = False

# if __name__ == '__main__':
#     # print("注册COM组件...")
#     # try:
#     #     import win32com.server.register
#     #     win32com.server.register.UseCommandLine(YOLOPlugin)
#     #     print("COM组件注册成功")
#     # except Exception as e:
#     #     print(f"注册失败: {e}")
    
#     yo=YOLOPlugin()
#     yo.start_detection()
#     time.sleep(10000)
######################################################################################
# yolo_component.py
import win32com.client
import pythoncom
import win32com.server.register
import cv2
import numpy as np
from PIL import ImageGrab
from ultralytics import YOLO
import os
import time
import sys

class YOLODetector:
    def __init__(self, model_path='resource/yolo12n.pt'):
        """初始化YOLO模型"""
        # 默认使用YOLOv8n模型，会自动下载
        try:
            self.model = YOLO(model_path)
            self.confidence_threshold = 0.5
        except Exception as e:
            print(f"初始化YOLO模型失败: {e}")
            raise
    
    def set_confidence(self, confidence):
        """设置置信度阈值"""
        self.confidence_threshold = confidence
    
    def detect_object(self, target_class=None, region=None, image_path=None):
        """
        检测目标对象
        """
        try:
            # 获取图像
            if image_path and os.path.exists(image_path):
                image = cv2.imread(image_path)
            else:
                if region:
                    x1, y1, x2, y2 = region
                    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
                else:
                    screenshot = ImageGrab.grab()
                image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            
            # 使用YOLO检测
            results = self.model(image, conf=self.confidence_threshold)
            
            detections = []
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    cls_id = int(box.cls[0])
                    cls_name = self.model.names[cls_id]
                    confidence = float(box.conf[0])
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    
                    # 如果指定了目标类别，则只返回匹配的结果
                    if target_class is None or str(cls_name).lower() == str(target_class).lower() or str(cls_id) == str(target_class):
                        detection = {
                            'class_id': cls_id,
                            'class_name': cls_name,
                            'confidence': confidence,
                            'bbox': (x1, y1, x2, y2),
                            'center_x': (x1 + x2) // 2,
                            'center_y': (y1 + y2) // 2,
                            'found': True
                        }
                        detections.append(detection)
            
            return {
                'success': True,
                'detections': detections,
                'count': len(detections)
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'detections': [],
                'count': 0
            }

class YOLOCOMComponent:
    """YOLO COM组件"""
    
    _public_methods_ = ['FindObject', 'GetObjectCount', 'GetObjectPosition', 
                       'SetConfidence', 'LoadModel', 'CaptureScreen', 'GetLastError']
    _public_attrs_ = ['version', 'last_error']
    _reg_progid_ = "YOLO.Detector"
    _reg_clsid_ = "{12345678-1234-5678-9012-345678901234}"
    
    def __init__(self):
        self.detector = YOLODetector()
        self.last_results = None
        self.version = "1.0"
        self.last_error = ""
    
    def LoadModel(self, model_path):
        """加载YOLO模型"""
        try:
            self.detector = YOLODetector(model_path)
            self.last_error = ""
            return True
        except Exception as e:
            self.last_error = f"加载模型失败: {e}"
            return False
    
    def SetConfidence(self, confidence):
        """设置置信度阈值 (0-1)"""
        try:
            self.detector.set_confidence(float(confidence))
            self.last_error = ""
            return True
        except Exception as e:
            self.last_error = f"设置置信度失败: {e}"
            return False
    
    def FindObject(self, target_class, region=None):
        """
        查找目标对象
        
        Args:
            target_class: 目标类别名称或ID
            region: 可选，检测区域 "x1,y1,x2,y2"
        
        Returns:
            是否找到对象
        """
        try:
            # 解析区域参数
            detect_region = None
            if region:
                coords = region.split(',')
                if len(coords) == 4:
                    detect_region = tuple(map(int, coords))
            
            # 执行检测
            result = self.detector.detect_object(target_class, detect_region)
            self.last_results = result
            self.last_error = ""
            
            return result['count'] > 0
            
        except Exception as e:
            self.last_error = f"检测失败: {e}"
            return False
    
    def GetObjectCount(self):
        """获取检测到的对象数量"""
        if self.last_results and self.last_results['success']:
            return self.last_results['count']
        return 0
    
    def GetObjectPosition(self, index=0):
        """
        获取对象位置
        
        Args:
            index: 对象索引
            
        Returns:
            位置字符串 "x,y" 或空字符串
        """
        if (self.last_results and self.last_results['success'] and 
            self.last_results['detections'] and index < len(self.last_results['detections'])):
            detection = self.last_results['detections'][index]
            return f"{detection['center_x']},{detection['center_y']}"
        return ""
    
    def CaptureScreen(self, filename):
        """截取屏幕并保存"""
        try:
            screenshot = ImageGrab.grab()
            screenshot.save(filename)
            self.last_error = ""
            return True
        except Exception as e:
            self.last_error = f"截屏失败: {e}"
            return False
    
    def GetLastError(self):
        """获取最后错误信息"""
        return self.last_error

# 直接在 __name__ == "__main__" 中处理注册和注销
if __name__ == '__main__':

    print("正在注册YOLO COM组件...")
    try:
        # 使用win32com.server.register注册组件
        win32com.server.register.UseCommandLine(YOLOCOMComponent)
        print("YOLO COM组件注册成功!")
        print("可以在按键精灵中使用: Set YOLO = CreateObject(\"YOLO.Detector\")")
    except Exception as e:
        print(f"注册失败: {e}")
        print("请确保以管理员身份运行此脚本")
