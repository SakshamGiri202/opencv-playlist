import cv2

cap = cv2.VideoCapture('/home/shaggy/Public/opencv-playlist/Resources/Videos/dog.mp4')  # Change to your video path

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    cv2.imshow('Video', frame)
    
    # This line was missing - it's essential!
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


   