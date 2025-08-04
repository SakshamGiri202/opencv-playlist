import numpy as np
import cv2 as cv
import os

# Use built-in Haar cascade instead of custom file
haar_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Check if cascade loaded successfully
if haar_cascade.empty():
    print("Error: Could not load Haar cascade!")
    print("Make sure opencv-contrib-python is installed:")
    print("pip install opencv-contrib-python")
    exit(1)

# Fixed people names (corrected spellings)
people = ["Ben Affleck", "Elton John", "Jerry Seinfeld", "Madonna", "Mindy Kaling"]

# Check if trained model exists
model_path = "face_trained.yml"
if not os.path.exists(model_path):
    print(f"Error: Trained model '{model_path}' not found!")
    print("Please run the training script first to create the model.")
    exit(1)

# Load the trained face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
try:
    face_recognizer.read(model_path)
    print("Successfully loaded trained model")
except Exception as e:
    print(f"Error loading trained model: {e}")
    exit(1)

# Fixed image path (use forward slashes or proper raw string)
img_path = r"../Resources/Faces/val/madonna/1.jpg"
# Alternative: img_path = '../Resources/Faces/val/elton_john/1.jpg'

# Check if image file exists
if not os.path.exists(img_path):
    print(f"Error: Image file '{img_path}' not found!")
    print("Please check the file path and ensure the image exists.")
    exit(1)

# Load and check image
img = cv.imread(img_path)
if img is None:
    print(f"Error: Could not load image from '{img_path}'")
    exit(1)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

# Detect faces in the image
faces_rect = haar_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=4,
    minSize=(30, 30),  # Added minimum size to avoid tiny false detections
)

print(f"Found {len(faces_rect)} face(s) in the image")

if len(faces_rect) == 0:
    print("No faces detected in the image!")
    print("Try adjusting the image or cascade parameters.")
else:
    # Process each detected face
    for i, (x, y, w, h) in enumerate(faces_rect):
        faces_roi = gray[y : y + h, x : x + w]

        # Predict the face
        label, confidence = face_recognizer.predict(faces_roi)

        # Lower confidence = better match (LBPH returns distance, not similarity)
        print(
            f"Face {i + 1}: Predicted as {people[label]} with confidence {confidence:.2f}"
        )

        # Add confidence threshold for better accuracy
        if confidence < 100:  # Adjust threshold as needed
            predicted_name = people[label]
            color = (0, 0, 255)  # Green for confident prediction
        else:
            predicted_name = "Unknown"
            color = (0, 0, 255)  # Red for uncertain prediction

        # Add text with name and confidence
        text = f"{predicted_name} ({confidence:.1f})"

        # Calculate text position (above the rectangle)
        text_y = y - 10 if y - 10 > 10 else y + h + 25

        cv.putText(
            img, text, (x, text_y), cv.FONT_HERSHEY_COMPLEX, 0.7, color, thickness=2
        )
        cv.rectangle(img, (x, y), (x + w, y + h), color, thickness=2)

# Display the result
cv.imshow("Detected Face", img)
print("Press any key to close the windows...")
cv.waitKey(0)
cv.destroyAllWindows()
