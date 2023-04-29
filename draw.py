import cv2 as cv
import numpy as np

blank = np.zeros((1080, 2000, 3), dtype='uint8')

# cv.imshow("Blank",blank)

blank[200:300, 300:400] = 0, 255, 0

cv.imshow("Green", blank)
#
# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (147, 255, 0), thickness=10  )
# # cv.imshow('Rectangle', blank)
#
# # line
# cv.line(blank, (100,200), (300,400), (255,255,25), thickness=3)
# # cv.imshow('Line', blank)
#
# # putting text
# cv.putText(blank, 'Hello Suckers', (300,400), cv.FONT_HERSHEY_TRIPLEX, 5.0, (200,200,200), 1)
# cv.imshow('Text', blank)
#
cv.waitKey(0)