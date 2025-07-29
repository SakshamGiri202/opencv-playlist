import cv2 as cv 

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    deminsion = (width, height)

    return cv.resize(frame, deminsion, interpolation=cv.INTER_AREA)


# def changeRes(width, height):
#     # for live video only
#     capture.set(3, width)
#     capture.set(4, height)




img = cv.imread('/home/shaggy/Public/opencv-playlist/Resources/Photos/cat.jpg')
img_resized = rescaleFrame(img, scale=0.2)
# Display image window named 'Cat'
cv.imshow('Cat', img)
cv.imshow('reszied img', img_resized)

# Wait indefinitely until key press
cv.waitKey(0)

# Close all windows
cv.destroyAllWindows()