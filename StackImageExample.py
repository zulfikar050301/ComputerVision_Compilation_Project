import cv2
import cvzone

cap = cv2.VideoCapture(0)

while True:

    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgSmall = cv2.resize(img, (0, 0), None, 0.1, 0.1)

    imgBig = cv2.resize(img, (0, 0), None, 3, 3)

    imgCanny = cv2.Canny(imgGray, 50, 150)

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    imgList = [img, imgGray, imgCanny, imgSmall, imgBig, imgHSV]

    stackedImg = cvzone.stackImages(imgList, 3, 0.7)

    cv2.imshow("stackedImg",stackedImg)

    cv2.imshow("Img",img)
    cv2.imshow("imgGray",imgGray)
    cv2.imshow("imgSmall",imgSmall)
    cv2.imshow("imgBig",imgBig)
    cv2.imshow("imgCanny",imgCanny)
    cv2.imshow("imgHSV",imgHSV)

    cv2.waitKey(1)