import cv2 as cv

img = cv.imread("/home/shaggy/Public/opencv-playlist/Resources/Photos/cat.jpg")

# cv.imshow("Cat", img)

# convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# cv.imshow("gray", gray)

# blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# edge cascade
canny = cv.Canny(blur, 125, 75)
cv.imshow("canny edge", canny)

# dilated the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("dilated", dilated)

# eroding
#eroded = cv.erode(dilated, (3, 3), iteration=3)
#cv.imshow("eroded", eroded)

# resize

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# cropped

cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)
cv.destroyAllWindows()
