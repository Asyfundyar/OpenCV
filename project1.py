import cv2
import numpy as np

fW = 640
fH = 480

cam = cv2.VideoCapture(0)

cam.set(3, fW)
cam.set(4, fH)
cam.set(10, 150)


def findcolor(img, colors):
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imghsv, lower, upper)
        cv2.imshow("Orange", mask)  # will generate different windows for each color


colors = [[5, 107, 0, 19, 255, 255]]  # orange

while True:
    success, img = cam.read()
    cv2.imshow("Video", img)
    findcolor(img, colors)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break;
