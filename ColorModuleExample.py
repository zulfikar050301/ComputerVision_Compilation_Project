import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

myColorFinder = ColorFinder(trackBar=True)

cap = cv2.VideoCapture(0)


cap.set(3, 640)
cap.set(4, 480)

hasVals = {'hmin':10, 'smin':55, 'vmin':215, 'hmax': 42, 'smax':255, 'vmax':255}

while True:

    success, img = cap.read()

    imgOrange, mask = myColorFinder.update(img, hasVals)

    imgStack = cvzone.stackImages([img, imgOrange, mask], 3, 1)

    cv2.imshow("Image Stack", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break