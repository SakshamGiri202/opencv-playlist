import cv2 as cv
import os

# Check if image exists
img_path = "../Resources/Photos/group 1.jpg"
if not os.path.exists(img_path):
    print(f"Error: Image file '{img_path}' not found!")
    exit(1)

# Load image
img = cv.imread(img_path)
if img is None:
    print(f"Error: Could not load image from '{img_path}'")
    exit(1)

cv.imshow("Group of 5 people", img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# Fix the Haar cascade path - use built-in cascade
# Your original path "/haar_face.xml" is incorrect (starts with /)
cascade_path = cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
haar_cascade = cv.CascadeClassifier(cascade_path)

# Check if cascade loaded successfully
if haar_cascade.empty():
    print(f"Error: Could not load Haar cascade from {cascade_path}")
    print("Make sure opencv-contrib-python is installed: pip install opencv-contrib-python")
    exit(1)

# Detect faces (increased minNeighbors for better accuracy)
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f"Number of faces found = {len(faces_rect)}")

# Draw rectangles around faces - fix the tuple unpacking
for (x, y, w, h) in faces_rect:  # Need parentheses around tuple
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Detected Faces", img)
cv.waitKey(0)
cv.destroyAllWindows()