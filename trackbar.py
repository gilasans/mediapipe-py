import numpy as np
import cv2 as cv

img = np.zeros((300,400,3), np.uint8)
cv.namedWindow('image')

def nothing(x):
    pass

cv.createTrackbar('R','image',70,255,nothing)
cv.createTrackbar('G','image',40,255,nothing)
cv.createTrackbar('B','image',200,255,nothing)

while True:
    img[:] = 0  

    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')

    cv.rectangle(img, (100,100), (200,200), (b,g,r), -1)

    cv.imshow('image', img)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()