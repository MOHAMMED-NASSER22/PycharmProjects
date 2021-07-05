import cv2

FramWidth = 450
FramHight = 480
cap = cv2.VideoCapture(0)
cap.set(3,FramWidth)
cap.set(4,FramHight)
cap.set(10,100)
while True:
    success , img = cap.read()
    imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    cv2.imshow("video",imgGray)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
