import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

print("reading ImageAt")
path = 'ImageAt'
images = []
Names = []


def LoadImages():
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        Names.append(os.path.splitext(cl)[0])
    print(Names)


def findEncoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendce(name):
    with open('attendance.csv', 'r+') as f:
        myDateList = f.readlines()
        nameList = []
        for line in myDateList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


# def getFrame():
#
#     while True:
#         _, img = cam.read()
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     return img
#     cam.release()
#     cv2.destroyAllWindows()

def show():
    while True:
        img1 = cam.read()
        cv2.imshow("show", img1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def faceRecognition():
    cam = cv2.VideoCapture(0)
    # #320x240
    # cap.set(3, 320)
    # cap.set(4, 400)
    while True:
        _, img = cam.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2GRAY)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = Names[matchIndex].upper()
                # print(name)
                global y1, x2, y2, x1
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 2)
                # markAttendce(name)
            else:
                name = 'UNKNOWN'
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, .9, (255, 255, 255), 2)
            print(faceLoc)
        cv2.imshow('faceRecognition', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break




LoadImages()
print('start encoding ')
encodeListKnown = findEncoding(images)
print('encoding complete')
faceRecognition()
print("exiting program")




