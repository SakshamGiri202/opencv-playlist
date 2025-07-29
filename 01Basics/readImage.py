import cv2 as cv


# Thsi finds and Load image from file path
# img_path = '/home/shaggy/Public/opencv-playlist/Resources/Photos/cat.jpg'
img = cv.imread('/home/shaggy/Public/opencv-playlist/Resources/Photos/cat.jpg')

# Display image window named 'Cat'
cv.imshow('Cat', img)

# Wait indefinitely until key press
cv.waitKey(0)

# Close all windows
cv.destroyAllWindows()
