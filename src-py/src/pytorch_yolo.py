# from ultralytics import YOLO

# # 加载预训练模型，如轻量级的yolov12n.pt
# model = YOLO('resource/yolo12n.pt')
# # 开始训练
# results = model.train(
#     data='dataset.yaml',  # 数据集配置文件的路径
#     epochs=100,           # 训练轮数
#     imgsz=640,            # 输入图像尺寸
#     batch=16,             # 批量大小
#     device=0,             # 使用GPU 0，如果是CPU则设为 'cpu'
#     optimizer='SGD',      # 优化器，如SGD, Adam, AdamW等
#     lr0=0.001,            # 初始学习率
#     patience=50           # 早停的等待epoch数
# )
#################################################################
import cv2
cap = cv2.VideoCapture(0)  # 同样，如果0不行，尝试1,2...
if cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print("摄像头可以正常读取！")
        cv2.imshow('Test Frame', frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("无法从摄像头读取帧。")
else:
    print("无法打开摄像头。")
cap.release()