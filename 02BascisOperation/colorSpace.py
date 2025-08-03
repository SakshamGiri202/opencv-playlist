import cv2 as cv
import matplotlib.pyplot as plt

img_path = "/home/shaggy/Public/opencv-playlist/Resources/Photos/cat.jpg"
img = cv.imread(img_path)

cv.imshow("cat", img)

# BGR to gray
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)
#

# BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("hsv", hsv)

# BGR TO lAB
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("lab", lab)

# BGR to RGB
RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", RGB)

# HSV to BGR
hsv_rgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow("hsv --> bgr", hsv_rgr)

# plt.imshow(RGB)
# plt.show()


# Wait indefinitely until key press
cv.waitKey(0)
# Close all windows
cv.destroyAllWindows()
