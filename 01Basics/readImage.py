import cv2 as cv

# This  finds and Load image from file ath
mg_path = "/home/shaggy/Public/opencv-playlist/Resources/Photos/cat.jpg"
img = cv.imread(img_path)

# Display image window named 'Cat'
cv.imshow("Cat", img)

# Wait indefinitely until key press
cv.waitKey(0)

# Close all windows
cv.destroyAllWindows()
