import cv2
import numpy as np

img = cv2.imread('/home/shaggy/Public/opencv-playlist/Resources/Photos/park.jpg')
cv2.imshow("cat", img)

# 1. Translation (Shifting)
#rows, cols = img.shape[:2]
# M = np.float32([[1, 0, 50], [0, 1, 25]])  # shift 50 px right and 25 px down
# dst = cv2.warpAffine(img, M, (cols, rows))
#cv2.imshow('Translated Image', dst)


# 2. Rotation
# center = (cols // 2, rows // 2)
# angle = 180  # degrees
# scale = 1.0
# M = cv2.getRotationMatrix2D(center, angle, scale)
# rotated = cv2.warpAffine(img, M, (cols, rows))
# cv2.imshow("Rotation", rotated)

# 3. Scaling (Resizing)
resized = cv2.resize(img, (400, 300), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized Image', resized)
enlarged = cv2.resize(resized,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
cv2.imshow('enlarged Image', enlarged)


cv2.waitKey(0)
cv2.destroyAllWindows()