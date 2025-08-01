import cv2
import numpy as np

img = cv2.imread("/home/shaggy/Public/opencv-playlist/Resources/Photos/park.jpg")
cv2.imshow("cat", img)

# 1. Translation (Shifting)
# rows, cols = img.shape
# M = np.float32([[1, 0, 50], [0, 1, 25]])  # shift 50 px right and 25 px down
# dst = cv2.warpAffine(img, M, (cols, rows))
# cv2.imshow('Translated Image', dst)


# 2. Rotation
# center = (cols // 2, rows // 2)
# angle = 180  # degrees
# scale = 1.0
# M = cv2.getRotationMatrix2D(center, angle, scale)
# rotated = cv2.warpAffine(img, M, (cols, rows))
# cv2.imshow("Rotation", rotated)

# 3. Scaling (Resizing)
# resized = cv2.resize(img, (400, 300), interpolation=cv2.INTER_CUBIC)
# cv2.imshow('Resized Image', resized)
# enlarged = cv2.resize(resized,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
# cv2.imshow('enlarged Image', enlarged)


# 4.Translation
# def Translation(img, x, y):
#     TransMat = np.float32([[1, 0, x], [0, 1, y]])
#     demension = (img.shape[1], img.shape[0])
#     return cv2.warpAffine(img, TransMat, demension)
#

# -x --> left
# -y --> up
# x --> right
# y --> down
#
# translated = Translation(img, 100, 100)
# cv2.imshow("Translation", translated)


# def Rotation(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
#
#     if rotPoint is None:
#         rotPoint = (width // 2, height // 2)
#     rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
#     demension = (width, height)
#     return cv2.warpAffine(img, rotMat, demension)
#
#
# rotated = Rotation(img, -45)
# cv2.imshow("rotated", rotated)

# 5. flip
flip = cv2.flip(img, -1)
cv2.imshow("flip", flip)


cv2.waitKey(0)
cv2.destroyAllWindows()

