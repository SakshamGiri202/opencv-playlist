import cv2 as cv
from numpy import median


img_path = "/home/shaggy/Public/opencv-playlist/Resources/Photos/group 1.jpg"
img = cv.imread(img_path)
cv.imshow("Group", img)


# Averaging
avg = cv.blur(img, (7, 7))
cv.imshow("average", avg)

# Gaussian blur
gaus = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("gaus", gaus)

# Median blur
medBlur = cv.medianBlur(img, 3)
cv.imshow("medBlur", medBlur)

# bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral", bilateral)


cv.waitKey(0)
cv.destroyAllWindows()
