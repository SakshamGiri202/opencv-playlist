# pylint:disable=no-member
import os
import cv2 as cv
import numpy as np

# Fixed people names (corrected spellings)
people = ["Ben Affleck", "Elton John", "Jerry Seinfeld", "Madonna", "Mindy Kaling"]

# Fixed directory path (use forward slashes or raw string properly)
DIR = r"../Resources/Faces/train"  # Fixed backslash issue
# Alternative: DIR = '../Media Files/Faces/train'

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

# Check if directory exists
if not os.path.exists(DIR):
    print(f"Error: Directory '{DIR}' does not exist!")
    print("Please create the directory structure and add training images.")
    exit(1)

features = []
labels = []


def create_train():
    """Create training data from images in subdirectories"""
    total_images = 0
    processed_images = 0

    for person in people:
        path = os.path.join(DIR, person)

        # Check if person's directory exists
        if not os.path.exists(path):
            print(f"Warning: Directory for '{person}' not found at '{path}'")
            continue

        label = people.index(person)
        print(f"Processing images for {person} (label: {label})...")

        person_images = 0
        for img_file in os.listdir(path):
            # Only process image files
            if not img_file.lower().endswith(
                (".png", ".jpg", ".jpeg", ".bmp", ".tiff")
            ):
                continue

            img_path = os.path.join(path, img_file)
            total_images += 1

            # Read image
            img_array = cv.imread(img_path)
            if img_array is None:
                print(f"Warning: Could not read image '{img_path}'")
                continue

            # Convert to grayscale
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Detect faces
            faces_rect = haar_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=4,
                minSize=(30, 30),  # Added minimum face size
            )

            # Process each detected face
            for x, y, w, h in faces_rect:
                faces_roi = gray[y : y + h, x : x + w]
                features.append(faces_roi)
                labels.append(label)
                person_images += 1
                processed_images += 1

        print(f"  Found {person_images} face(s) for {person}")

    print(f"\nTotal images processed: {processed_images} out of {total_images}")
    return processed_images > 0


# Create training data
if create_train():
    print("Training data creation completed ---------------")

    # Convert to numpy arrays
    features = np.array(features, dtype="object")
    labels = np.array(labels)

    print(f"Features shape: {features.shape}")
    print(f"Labels shape: {labels.shape}")

    # Create and train the face recognizer
    try:
        face_recognizer = cv.face.LBPHFaceRecognizer_create()

        # Train the recognizer
        print("Training the face recognizer...")
        face_recognizer.train(features, labels)

        # Save the trained model and data
        face_recognizer.save("face_trained.yml")
        np.save("features.npy", features)
        np.save("labels.npy", labels)

        print("Training completed successfully!")
        print("Saved files:")
        print("- face_trained.yml (trained model)")
        print("- features.npy (training features)")
        print("- labels.npy (training labels)")

    except Exception as e:
        print(f"Error during training: {e}")
        print("Make sure opencv-contrib-python is installed:")
        print("pip install opencv-contrib-python")

else:
    print("No training data found! Please check your directory structure.")
    print(f"Expected structure:")
    print(f"{DIR}/")
    for person in people:
        print(f"  {person}/")
        print(f"    image1.jpg")
        print(f"    image2.jpg")
        print(f"    ...")
