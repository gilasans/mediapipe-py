import cv2
img =cv2.imread('gambar.jpg',1)
cv2.imshow('image',img)
key=cv2.waitKey(0)
if key==ord('s'):
 cv2.imwrite("gambar2.jpg", img)
cv2.destroyAllWindows()