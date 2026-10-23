import cv2

img1 = cv2.imread('gambar.jpg', 1)
img2 = cv2.imread('gambar2.jpg', 1)

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
dest1 = cv2.bitwise_and(img2, img1)

cv2.imshow('A', img1)
cv2.imshow('B', img2)
cv2.imshow('AND', dest1)
cv2.waitKey(0)
cv2.destroyAllWindows()