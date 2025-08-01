import cv2
import numpy as np


img = cv2.imread("/home/shaggy/Public/opencv-playlist/Resources/Photos/park.jpg")
cv2.imshow("cat", img)


black = np.zeros(img.shape, dtype="uint8")
cv2.imshow("black", black)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

canny = cv2.Canny(img, 125, 175)
cv2.imshow("canny edge", canny)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f"{len(contours)} contour(s) fount!")

cv2.drawContours(black, contours, -1, (0, 0, 255), 1)
cv2.imshow("contours draw", black)

cv2.waitKey(0)
cv2.destroyAllWindows()
