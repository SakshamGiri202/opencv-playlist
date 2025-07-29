### 1. Introduction & Setup

**What is OpenCV?**  
OpenCV (Open Source Computer Vision Library) is a popular open-source library used for computer vision and image processing tasks. It provides numerous functions to work with images and videos, including reading, modifying, and analyzing visual data.

**Installing OpenCV and dependencies:**  
To get started, you need to install the following Python packages:

- `opencv-contrib-python`: This includes the main OpenCV modules and additional contributed modules.
- `caer`: A utility library Jason uses for the capstone project.
- `numpy`: For numerical operations, often used to handle images as arrays.

You can install these via pip:

```bash
pip install opencv-contrib-python
pip install caer
pip install numpy
```

Also, ensure you have **Python 3.7 or higher** installed on your system.

### 2. Reading Images, Videos, and Webcam

**Reading an Image**

You can load an image using `cv2.imread()` and display it with `cv2.imshow()`:

```python
import cv2

# Load image from file path
img = cv2.imread('photos/cat.jpg')

# Display image window named 'Cat'
cv2.imshow('Cat', img)

# Wait indefinitely until key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
```

**Reading a Video File**

To read and display a video, use `cv2.VideoCapture()` in a loop:

```python
import cv2

capture = cv2.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()  # Read one frame
    if not isTrue:
        break  # Exit loop if no frame is returned
    
    cv2.imshow('Video', frame)
    
    # Press 'd' key to break and close video window
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()
```

**Using the Webcam**

To capture live video from the webcam:

```python
import cv2

capture = cv2.VideoCapture(0)  # 0 is usually the default camera

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):  # Press 'q' to quit
        break

capture.release()
cv2.destroyAllWindows()
```

