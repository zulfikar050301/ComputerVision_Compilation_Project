from cvzone.Utils import rotateImage
import cv2

cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()

    #Rotate the image by 60 degrees without keeping the size
    imgRotated60 = rotateImage(img, 60, scale=1,
                               keepSize=False) #Rotate image 60 degrees, scale it by 1, and don't keep the original

    #Rotate the image by 60 degree while keeping the size
    imgRotated60KeepSize = rotateImage(img, 60, scale=1,
                                       keepSize=True) #Rotate image 60 degrees, scale it by 1, and keep the original

    cv2.imshow("img", img)

    cv2.imshow("imgRotated60", imgRotated60)
    
    cv2.imshow("imgRotated60KeepSize", imgRotated60KeepSize)

    cv2.waitKey()

