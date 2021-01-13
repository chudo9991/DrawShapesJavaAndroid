import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

# Так забираем из готового видео
# cap = cv2.VideoCapture("video.mp4")
faces_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(3, 640)
cap.set(4, 480)

print(cap.set(3, 1280), cap.set(4, 700))

while True:
    ret, frame = cap.read()

    faces = faces_cascade.detectMultiScale(frame, 1.3, 5)

    # # Рисуем квадраты вокруг лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow("hi", frame)
    cv2.waitKey()

cap.release()
cv2.destroyWindow("hi")
