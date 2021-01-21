from imageai.Detection import VideoObjectDetection
import os
import cv2
from matplotlib import pyplot as plt

color_index = {'bus': 'red', 'handbag': 'steelblue', 'giraffe': 'orange', 'spoon': 'gray', 'cup': 'yellow',
               'chair': 'green', 'elephant': 'pink', 'truck': 'indigo', 'motorcycle': 'azure', 'refrigerator': 'gold',
               'keyboard': 'violet', 'cow': 'magenta', 'mouse': 'crimson', 'sports ball': 'raspberry',
               'horse': 'maroon', 'cat': 'orchid', 'boat': 'slateblue', 'hot dog': 'navy', 'apple': 'cobalt',
               'parking meter': 'aliceblue', 'sandwich': 'skyblue', 'skis': 'deepskyblue', 'microwave': 'peacock',
               'knife': 'cadetblue', 'baseball bat': 'cyan', 'oven': 'lightcyan', 'carrot': 'coldgrey',
               'scissors': 'seagreen', 'sheep': 'deepgreen', 'toothbrush': 'cobaltgreen', 'fire hydrant': 'limegreen',
               'remote': 'forestgreen', 'bicycle': 'olivedrab', 'toilet': 'ivory', 'tv': 'khaki',
               'skateboard': 'palegoldenrod', 'train': 'cornsilk', 'zebra': 'wheat', 'tie': 'burlywood',
               'orange': 'melon', 'bird': 'bisque', 'dining table': 'chocolate', 'hair drier': 'sandybrown',
               'cell phone': 'sienna', 'sink': 'coral', 'bench': 'salmon', 'bottle': 'brown', 'car': 'silver',
               'bowl': 'maroon', 'tennis racket': 'palevilotered', 'airplane': 'lavenderblush', 'pizza': 'hotpink',
               'umbrella': 'deeppink', 'bear': 'plum', 'fork': 'purple', 'laptop': 'indigo', 'vase': 'mediumpurple',
               'baseball glove': 'slateblue', 'traffic light': 'mediumblue', 'bed': 'navy', 'broccoli': 'royalblue',
               'backpack': 'slategray', 'snowboard': 'skyblue', 'kite': 'cadetblue', 'teddy bear': 'peacock',
               'clock': 'lightcyan', 'wine glass': 'teal', 'frisbee': 'aquamarine', 'donut': 'mincream',
               'suitcase': 'seagreen', 'dog': 'springgreen', 'banana': 'emeraldgreen', 'person': 'honeydew',
               'surfboard': 'palegreen', 'cake': 'sapgreen', 'book': 'lawngreen', 'potted plant': 'greenyellow',
               'toaster': 'ivory', 'stop sign': 'beige', 'couch': 'khaki'}

execution_path = os.getcwd()
resized = False

def forFrame(frame_number, output_array, output_count, returned_frame):
    plt.clf()

    this_colors = []
    labels = []
    sizes = []

    counter = 0

    for eachItem in output_count:
        counter += 1
        sizes.append(output_count[eachItem])
        labels.append(eachItem + " = " + str(output_count[eachItem]))
        this_colors.append(color_index[eachItem])

    global resized

    if (resized == False):
        manager = plt.get_current_fig_manager()
        manager.resize(width=1000, height=600)
        resized = True

    plt.subplot(1, 1, 1)
    plt.title("Frame : " + str(frame_number))
    plt.axis("off")
    plt.imshow(returned_frame, interpolation="none")

    plt.pause(0.01)

def forSeconds(second_number, output_arrays, count_arrays, average_output_count, n):
    print("SECOND : ", second_number)
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last second: ", average_output_count)
    print("------------END OF A SECOND --------------")

def forMinute(minute_number, output_arrays, count_arrays, average_output_count, n):
    print("MINUTE : ", minute_number)
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last minute: ", average_output_count)
    print("------------END OF A MINUTE --------------")

cap = cv2.VideoCapture("rtsp://stream:ljOL8fDu@10.0.231.60")

# cap = cv2.VideoCapture("rtsp://stream:LdXq1Fiz@10.1.56.58")

cap.set(3, 800)
cap.set(4, 600)

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolo.h5")
# detector.setModelTypeAsTinyYOLOv3()
# detector.setModelPath("yolo-tiny.h5")

detector.loadModel(detection_speed="fast")

try:
    video = detector.detectObjectsFromVideo(
        camera_input=cap,
        frames_per_second=5,
        log_progress=True,
        minimum_percentage_probability=60,
        # detection_timeout=120,
        per_frame_function=forFrame,
        per_second_function=forSeconds,
        per_minute_function=forMinute,
        save_detected_video=True,
        output_file_path=os.path.join(execution_path, "output"),
        return_detected_frame=True
    )

except cv2.error as e:
    print(e)

cap.release()
cv2.destroyAllWindows()