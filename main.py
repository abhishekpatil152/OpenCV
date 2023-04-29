import cv2 as cv
import numpy as np

#img = cv.imread('photos/cats/cat1.jpg')


#cv.imshow('Cat', img)
capture = cv.VideoCapture('photos/dogs/dog1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()