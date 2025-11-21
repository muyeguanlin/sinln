# import win32com.server.register
# import cv2
# import numpy as np
# from PIL import ImageGrab
# from ultralytics import YOLO

# class YOLOCOMComponent:
#     """YOLO COM组件"""
    
#     _public_methods_ = ['FindObject']
#     _reg_progid_ = "YOLO.Detector"
#     _reg_clsid_ = "{12345678-1234-5678-9012-345678901234}"
    
#     def __init__(self):
#         self.model = YOLO('./resource/yolo12n.pt')
#         self.confidence_threshold = 0.5

#         self.last_detection_time = 0
#         self.detection_interval = 2.0  # 检测间隔，秒
#         self.show_results = False  # 默认不显示结果
    
#     def FindObject(self, target_class, region=None):
#         """查找目标对象并显示检测结果"""
#         try:
#             # 获取屏幕图像
#             if region:
#                 coords = region.split(',')
#                 if len(coords) == 4:
#                     x1, y1, x2, y2 = map(int, coords)
#                     screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
#                 else:
#                     screenshot = ImageGrab.grab()
#             else:
#                 screenshot = ImageGrab.grab()
            
#             image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)##将PIL截图的RGB格式转换为BGR格式，因为YOLO模型通常期望BGR格式的输入
            
#             # YOLO检测
#             results = self.model(image, conf=self.confidence_threshold)
            
#             # 在图像上绘制检测结果
#             annotated_image = results[0].plot()
            
#             # 显示检测结果
#             cv2.imshow('YOLO Detection Results', annotated_image)
#             cv2.waitKey(1)  # 显示图像，等待1毫秒
            
#             detections = []
#             for result in results:
#                 boxes = result.boxes
#                 for box in boxes:
#                     cls_id = int(box.cls[0])
#                     cls_name = self.model.names[cls_id]
#                     confidence = float(box.conf[0])
#                     x1, y1, x2, y2 = map(int, box.xyxy[0])
                    
#                     if str(cls_name).lower() == str(target_class).lower() or str(cls_id) == str(target_class):
#                         detection = {
#                             'class_id': cls_id,
#                             'class_name': cls_name,
#                             'confidence': confidence,
#                             'center_x': (x1 + x2) // 2,
#                             'center_y': (y1 + y2) // 2
#                         }
#                         detections.append(detection)
            
#             return len(detections) > 0
            
#         except Exception as e:
#             print(f"检测错误: {e}")
#             return False

# if __name__ == '__main__':
#     win32com.server.register.UseCommandLine(YOLOCOMComponent)

################################################################################################################
import win32com.server.register
import cv2
import numpy as np
from PIL import ImageGrab
from ultralytics import YOLO

class YOLOCOMComponent:
    """YOLO COM组件"""
    
    _public_methods_ = ['FindObject']
    _reg_progid_ = "YOLO.Detector"
    _reg_clsid_ = "{12345678-1234-5678-9012-345678901234}"
    
    def __init__(self):
        self.model = YOLO('./resource/yolo12n.pt')
        self.confidence_threshold = 0.5

        self.last_detection_time = 0
        self.detection_interval = 2.0  # 检测间隔，秒
        self.show_results = False  # 默认不显示结果
    
    def FindObject(self, target_class, region=None):
        """查找目标对象并返回检测到的数量
        
        Args:
            target_class: 要查找的目标类别名称或ID
            region: 可选，检测区域 "x1,y1,x2,y2" 格式
            
        Returns:
            int: 检测到的目标对象数量
        """
        try:
            # 获取屏幕图像
            if region:
                coords = region.split(',')
                if len(coords) == 4:
                    x1, y1, x2, y2 = map(int, coords)
                    screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
                else:
                    screenshot = ImageGrab.grab()
            else:
                screenshot = ImageGrab.grab()
            
            image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            
            # YOLO检测
            results = self.model(image, conf=self.confidence_threshold)
            
            # 在图像上绘制检测结果
            annotated_image = results[0].plot()
            
            # 显示检测结果
            cv2.imshow('YOLO Detection Results', annotated_image)
            cv2.waitKey(1)  # 显示图像，等待1毫秒
            
            # 计算指定类别的检测数量
            detection_count = 0
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    cls_id = int(box.cls[0])
                    cls_name = self.model.names[cls_id]
                    
                    # 检查是否匹配目标类别
                    if str(cls_name).lower() == str(target_class).lower() or str(cls_id) == str(target_class):
                        detection_count += 1
            
            # 返回检测到的目标数量
            return detection_count
            
        except Exception as e:
            print(f"检测错误: {e}")
            return 0

if __name__ == '__main__':
    win32com.server.register.UseCommandLine(YOLOCOMComponent)