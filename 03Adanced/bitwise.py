import cv2 as cv
import numpy as np


blanlk = np.zeros((400, 400), dtype="uint8")

rectangle = cv.rectangle(blanlk.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blanlk.copy(), (200, 200), 200, 255, -1)


cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)


# bitwise and --> intersection region
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise_and", bitwise_and)

# bitwise_or  --> non-intersection and intersection region
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise_or", bitwise_or)

# bitwise_xor  --> non-intersection
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise_xor", bitwise_xor)


# bitwise_not
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwise_not", bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()
