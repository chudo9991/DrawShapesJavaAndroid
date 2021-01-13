import cv2  # импорт модуля cv2

# cap = cv2.VideoCapture("video.mp4") # из видео файла

cap = cv2.VideoCapture("rtsp://stream:ljOL8fDu@10.0.231.60")
# cap = cv2.VideoCapture(0);  # с веб камеры

cap.set(3, 640)  # установка размера окна
cap.set(4, 480)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():  # метод isOpened() выводит статус видеопотока

    diff = cv2.absdiff(frame1, frame2)  # нахождение разницы двух кадров

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # перевод кадров в Ч/Б

    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # фильтрация лишних контуров

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)  # метод для выделения кромки объекта белым цветом

    dilated = cv2.dilate(thresh, None, iterations=3)  # расширяет выделенную на предыдущем этапе область

    сontours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # нахождение массива контурных точек

    for contour in сontours:
        (x, y, w, h) = cv2.boundingRect(
            contour)  # преобразование массива из предыдущего этапа в кортеж из четырех координат

        # метод contourArea() по заданным contour точкам, здесь кортежу, вычисляет площадь зафиксированного объекта в каждый момент времени, это можно проверить
        # print(cv2.contourArea(contour))

        if cv2.contourArea(contour) < 1500:  # условие при котором площадь выделенного объекта меньше 700 px
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)  # получение прямоугольника из точек кортежа

    # cv2.drawContours(frame1, сontours, -1, (0, 255, 0), 2) # также можно было просто нарисовать контур объекта

    cv2.imshow("pic", frame1)
    frame1 = frame2  #
    ret, frame2 = cap.read()  #

    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()