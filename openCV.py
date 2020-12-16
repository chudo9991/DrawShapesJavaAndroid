# На 16 декабря 2020 надо было ставить numpy версии 1.19.3
# Для OpenCV - поставить opencv-python

# Цвета приходят в формате BRG (blue - red - green)

import cv2
import numpy as np

photo = cv2.imread("./34.jpg")

# Обрезка
#cropped = photo[10:300, 10:300] # Режет фото

# Поворот изображения
# (h,w,d) = photo.shape
# center = (w//2, h//2)
# X = cv2.getRotationMatrix2D(center, 180, 1.0)
# cropped = cv2.warpAffine(photo, X, (w,h))

# Масштабирование
# cropped = cv2.resize(photo, (100, 100), interpolation = cv2.INTER_AREA)

# Первод в grayscale
# cropped = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

# Перевод с ч/б
# ret, cropped = cv2.threshold(photo, 127, 255, 0)

# Сглаживание и размытие
# cropped = cv2.GaussianBlur(photo, (51,51), 0)

# Рисуем прямоугольник
# cropped = photo.copy()
# cv2.rectangle(cropped, (20,20), (200,200), (0,255,255), 10)

# Рисование линий
# cropped = photo.copy()
# cv2.line(cropped, (20,20), (400,400), (0,255,0), 5)

# Сделаем надпись - надо почитать мануал!
# cropped = photo.copy()
# v2.putText(cropped, "Hi!", (0,500), cv2.FONT_HERSHEY_SIMPLEX, 12, (0,255,0), 10)

cropped = photo.copy()

faces_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)

faces = faces_cascade.detectMultiScale (
    gray,
    scaleFactor=1.1,
    minNeighbors = 5,
    minSize = (10,10)
)
cv2.imshow("Dog", gray)

faces = faces_cascade.detectMultiScale (gray, 1.3, 5)

faces_detected = "Лиц обнаружено: " + format(len(faces))
print("Нашли лиц ",faces_detected)
#
# # Рисуем квадраты вокруг лиц
for (x, y, w, h) in faces:
    cv2.rectangle(cropped, (x, y), (x+w, y+h), (255, 255, 0), 2)

cv2.imshow("Dog", cropped)
cv2.waitKey()
cv2.destroyAllWindows()

