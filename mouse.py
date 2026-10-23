import cv2 as cv

def drawfunction(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 20, (0, 0, 255), -1)

img = cv.imread('gambar.jpg')
cv.namedWindow('image')
cv.setMouseCallback('image', drawfunction)

while True:
    cv.imshow('image', img)
    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()