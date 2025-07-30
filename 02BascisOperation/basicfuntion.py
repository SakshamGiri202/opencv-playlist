import cv2 as cv

img = cv.imread("/home/shaggy/Public/opencv-playlist/Resources/Photos/cat.jpg")

cv.imshow("cat", img)

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow("gray", gray)

cv.waitKey(0)
cv.destroyAllWindows()

