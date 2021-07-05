import cv2

face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    faces = face_cascade.detectMultiScale(img, scaleFactor = 1.2, minNeighbors = 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 2500), 3)
        break

    cv2.imshow("video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
