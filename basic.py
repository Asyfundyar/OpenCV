import cv2
import numpy as np

"""
****For reading and displaying an image****
"""

img = cv2.imread("resources/example.jpg")
kernel = np.ones((5, 5), np.uint8)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (7, 7), 0)
canny = cv2.Canny(img, 150, 200)
dilation = cv2.dilate(canny, kernel, iterations=1)
erosion = cv2.erode(canny, dilation, iterations=1)

cv2.imshow("Output", img)
cv2.imshow("Gray image", gray)
cv2.imshow("Blur image", blur)
cv2.imshow("Canny image", canny)
cv2.imshow("Dilation image", dilation)
cv2.imshow("Erosion image", erosion)

cv2.waitKey(0)

"""
****For reading a video****
"""

vid = cv2.VideoCapture("resources/MVI_0020.MOV")

while True:
    success, img = vid.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

"""
****For reading from web cam****
"""

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
cam.set(10, 100)

while True:
    success, img = cam.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
"""
****For resizing and cropping images****
"""

print(img.shape) # prints the width, length, etc of an image

resize = cv2.resize(img, (700, 1000))
print(resize.shape)

cropped = img[150:800, 200:600]
print(resize.shape)

cv2.imshow("Image", img)
cv2.imshow("Resized Image", resize)
cv2.imshow("Cropped Image", cropped)
