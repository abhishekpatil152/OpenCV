import cv2 as cv

# img = cv.imread('photos\cats\cat1.jpg')
#
# cv.imshow('Cat',img)

def rescaleFrame(frame, scale):

    width = int(frame.shape[1]* scale)

    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA )

def changeRes(width , height):

    capture.set(10,width)
    capture.set(10,height)

# resized_image = rescaleFrame(img,scale=0.2)
# cv.imshow('Image',resized_image)
#
# cv.waitKey(0)

capture = cv.VideoCapture(0)

while True:
    isTrue , frame = capture.read()

    frame_resize = rescaleFrame(frame ,scale=2)

    cv.imshow('Dog',frame)
    cv.imshow('video Resized',frame_resize)

    if cv.waitKey(20 ) & 0xFF==ord('d'):
        break

capture.release()
capture.destroyallwindows

