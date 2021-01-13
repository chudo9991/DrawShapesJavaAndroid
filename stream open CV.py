from imageai.Detection import VideoObjectDetection
import os
import cv2

execution_path = os.getcwd()

cap = cv2.VideoCapture("rtsp://stream:ljOL8fDu@10.0.231.60")

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
detector.loadModel(detection_speed="fast")

video = detector.detectObjectsFromVideo(
    camera_input=cap,
    frames_per_second=10,
    log_progress=True,
    minimum_percentage_probability=60,
    detection_timeout=120,
    output_file_path=os.path.join(execution_path, "camera_detected_video"),
)