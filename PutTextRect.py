import cv2
import cvzone

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.rectangle(img, (80, 40), (300, 200), (255, 0, 255), cv2.FILLED)
    cv2.putText(img, "Zul", (100, 150), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 5)

    cvzone.putTextRect(img, "Zul", (200, 300), border=5, offset=20)

    cv2.imshow("Image", img)
    cv2.waitKey(1)