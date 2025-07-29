# OpenCV Playlist

This repository contains structured notes and code summaries based on the [OpenCV Course - Full Tutorial with Python](https://www.youtube.com/watch?v=oXlwWbU8l2o) by Jason Dsouza. The course covers everything from the very basics of image and video manipulation to advanced computer vision concepts. This README provides an organized overview, code highlights, and links to relevant resources.

## Table of Contents

- [Course Overview](#course-overview)
- [Course Topics](#course-topics)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Notebooks & Code](#notebooks--code)
- [Key Concepts and Examples](#key-concepts-and-examples)
    - [Section 1: Basics](#section-1-basics)
    - [Section 2: Advanced](#section-2-advanced)
    - [Section 3: Faces](#section-3-faces)
    - [Section 4: Capstone](#section-4-capstone)
- [References](#references)
- [License](#license)

## Course Overview

This course aims to teach **OpenCV** for Python from basics to advanced applications. The tutorial covers fundamental skills—like reading images and videos, transforming images, drawing on frames—as well as advanced topics such as face detection, recognition, and a deep learning-based vision project (“The Simpsons” character classifier)[1].

## Course Topics

- Installing OpenCV, Caer, and NumPy
- Reading and displaying images and videos
- Image resizing, rescaling, and transformations
- Drawing shapes and writing text on images
- Color spaces, channels, and blurring
- Bitwise operations, masking, and histograms
- Thresholding and edge detection
- Face detection & recognition
- Image cropping, ROI, and geometric transformations
- Deep learning for image classification (capstone project)

## Getting Started

### Prerequisites

- Python 3.7 or above (recommended)
- pip for installing packages

### Installation

```bash
pip install opencv-contrib-python
pip install caer
pip install numpy
```
> The `opencv-contrib-python` package contains both the main and extra OpenCV modules.  
> `caer` is a utility library used in the capstone project[1].

## Notebooks & Code

- Follow along with your custom Python scripts or Jupyter Notebooks.
- Reference code and datasets can be found in Jason’s [GitHub repository for the course](https://github.com/jasmcaus/opencv-course).

## Key Concepts and Examples

### Section 1: Basics

- **Reading Images:**
    ```python
    img = cv2.imread('photos/cat.jpg')
    cv2.imshow('Cat', img)
    cv2.waitKey(0)
    ```

- **Reading Video:**
    ```python
    capture = cv2.VideoCapture('videos/dog.mp4')
    while True:
        isTrue, frame = capture.read()
        cv2.imshow('Video', frame)
        if cv2.waitKey(20) & 0xFF == ord('d'):
            break
    capture.release()
    cv2.destroyAllWindows()
    ```

- **Resizing & Rescaling:**
    ```python
    def rescaleFrame(frame, scale=0.75):
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width, height)
        return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
    ```

- **Drawing on Images:**
    - Rectangles, circles, lines, text with `cv2.rectangle`, `cv2.circle`, `cv2.putText`
    - Creating blank images with NumPy


### Section 2: Advanced

- **Color Spaces and Channels**
    - Convert with `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`
- **Blurring**
    - `cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)`
- **Edge Detection**
    - `cv2.Canny(img, 125, 175)`
- **Dilate & Erode Edges**
    - `cv2.dilate(edges, (3,3), iterations=1)`
    - `cv2.erode(dilated, (3,3), iterations=1)`
- **Image Transformations**
    - Translation, rotation, flipping, cropping

### Section 3: Faces

- **Face Detection**: Using Haar Cascades
- **Face Recognition**: OpenCV's built-in recognizer

### Section 4: Capstone

- **Deep Learning Vision Model**: Classifying Simpsons characters using a CNN (with Caer).

## References

- [Course Video](https://www.youtube.com/watch?v=oXlwWbU8l2o)
- [Course GitHub Repo](https://github.com/jasmcaus/opencv-course)
- [Jason Dsouza on Twitter](https://twitter.com/jasmcaus)
- [Caer Library](https://github.com/jasmcaus/caer)

## License

This repository contains notes and code adapted from freely available YouTube and GitHub content shared by Jason Dsouza for educational purposes.

*Happy coding with OpenCV! Feel free to use these notes while working through the course or building your own computer vision projects.*

[1] https://www.youtube.com/watch?v=oXlwWbU8l2o