import cv2
import numpy as np

path = "Girl-Background.png"
img = cv2.imread(path)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 400, 400)

def empty(a):
    pass

cv2.createTrackbar("Hue Min","Trackbar",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbar",19,179,empty)
cv2.createTrackbar("Sat Min","Trackbar",110,255,empty)
cv2.createTrackbar("Sat Max","Trackbar",240,255,empty)
cv2.createTrackbar("Val Min","Trackbar",0,255,empty)
cv2.createTrackbar("Val Max","Trackbar",255,255,empty)

while True:
    h_min = cv2.getTrackbarPos("Hue Min","Trackbar")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbar")
    s_min = cv2.getTrackbarPos("Sat Min","Trackbar")
    s_max = cv2.getTrackbarPos("Sat Max","Trackbar")
    v_min = cv2.getTrackbarPos("Val Min","Trackbar")
    v_max = cv2.getTrackbarPos("Val Max","Trackbar")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    cv2.imshow("Output", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
