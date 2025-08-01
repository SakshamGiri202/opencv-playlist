import cv2

capture = cv2.VideoCapture(0)  # 0 is usually the default camera

def changeRes(width, height):
    # for live video only
    capture.set(6, width)
    capture.set(8, height)


while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):  # Press 'q' to quit
        break

capture.release()
cv2.destroyAllWindows()
