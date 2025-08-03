import cv2 as cv
import numpy as np

# This  finds and Load image from file path
img_path = "/home/shaggy/Public/opencv-playlist/Resources/Photos/group 1.jpg"
img = cv.imread(img_path)

# Display image window named 'Cat'
cv.imshow("group", img)

# b, g, r = cv.split(img)
#
# cv.imshow("blue", b)
# cv.imshow("green", g)
# cv.imshow("red", r)
#
#
#
#
# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)


blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow("Merged Image", merged)


cv.waitKey(0)
cv.destroyAllWindows()
