import cv2 as cv

capture = cv.VideoCapture(0)  # 0 is usually the default camera

def changeRes(width, height):
    # for live video only
    capture.set(6, width)
    capture.set(8, height)


while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    cv.imshow('Webcam', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):  # Press 'q' to quit
        break

capture.release()
cv.destroyAllWindows()
