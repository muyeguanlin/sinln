import win32com.server.register
import cv2
import numpy as np
from ultralytics import YOLO
import mss
import time

class YOLOCOMComponent:
    """YOLO COM组件"""
    
    # _public_methods_ = ['FindObject']
    # _reg_progid_ = "YOLO.Detector"
    # _reg_clsid_ = "{12345678-1234-5678-9012-345678901234}"
    
    def __init__(self):
        self.model = YOLO('./resource/yolo12n.pt')
        self.confidence_threshold = 0.5
        self.sct = mss.mss()  # 创建mss实例

        self.last_detection_time = 0
        self.detection_interval = 2.0  # 检测间隔，秒
        self.show_results = False  # 默认不显示结果
    
    def FindObject(self, target_class, region="0,0,1260,720"):
        """查找目标对象并返回检测到的数量
        
        Args:
            target_class: 要查找的目标类别名称或ID
            region: 可选，检测区域 "x1,y1,x2,y2" 格式
            
        Returns:
            int: 检测到的目标对象数量
        """
        try:
            # 使用mss获取屏幕图像
            if region:
                coords = region.split(',')
                if len(coords) == 4:
                    x1, y1, x2, y2 = map(int, coords)
                    monitor = {"left": x1, "top": y1, "width": x2 - x1, "height": y2 - y1}
                else:
                    # 如果没有提供有效的区域，使用整个屏幕
                    monitor = self.sct.monitors[1]  # 主显示器
            else:
                # 使用整个屏幕
                monitor = self.sct.monitors[1]  # 主显示器
            
            # 捕获屏幕
            screenshot = self.sct.grab(monitor)
            
            # 将mss截图转换为numpy数组
            image = np.array(screenshot)
            
            # 删除alpha通道（如果有）
            if image.shape[2] == 4:
                image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
            else:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # YOLO检测
            # results = self.model(image, conf=self.confidence_threshold)#只保留置信度大于等于0.5的检测结果。
            results = self.model(image)

            result = results[0]

            # # 可以访问的内容：
            # print(result.boxes)        # 边界框信息
            # print(result.boxes.xyxy)   # 边界框坐标 [x1, y1, x2, y2]
            # print(result.boxes.conf)   # 置信度分数
            # print(result.boxes.cls)    # 类别ID
            # print(result.names)        # 类别名称映射

            
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
    # win32com.server.register.UseCommandLine(YOLOCOMComponent)
    yo=YOLOCOMComponent()
    for _ in range(1000):
        x=yo.FindObject("person", "0,0,1260,720")
        print(f"查询到{x}个结果——————————————————")
        time.sleep(1)
