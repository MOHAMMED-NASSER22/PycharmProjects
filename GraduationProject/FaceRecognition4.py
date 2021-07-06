import cv2
import numpy as np
import face_recognition
import os
import threading
import time

print("reading ImageAt...")
path = 'ImageAt'
images = []
Names = []
cap = cv2.VideoCapture(0)
_, img = cap.read()
_, imgS = cap.read()
_, img = cap.read()
_, imgS = cap.read()

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


def show():
    while True:
        _, img1 = cap.read()
        cv2.imshow("LiveFeed", img1)
        if cv2.waitKey(10) & 0xFF == ord('s'):
            break


def faceRecognition():
    while True:
        time.sleep(1)
        _, img = cap.read()
        _, imgS = cap.read()
        # imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        # imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2GRAY)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(Outlist, encodeFace)
            faceDis = face_recognition.face_distance(Outlist, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)
            nameFlag = False  # there is no known face
            if matches[matchIndex]:
                nameFlag = True # there is known face
                name = Names[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name , (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 2)
                # cv2.putText(img, f'{name} {round(1 - (faceDis[matchIndex]), 2)}', (x1 + 6, y2 - 6),
                #             cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 2) # if i want to print the matches percent %
                # markAttendce(name)
                # faceloc1 = faceLoc
            else:
                name = 'UNKNOWN'
                print(name)
                y1, x2, y2, x1 = faceLoc
                # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, .9, (255, 255, 255), 2)
            if nameFlag:
                # print(faceLoc)
                X_Center = (x1+x2)/2
                Y_Center = (y1+y2)/2
                print( " X_Center :  " + str(X_Center) +  "  Y_Center :  "  + str(Y_Center))
        cv2.imshow('faceRecognition', img)
        if cv2.waitKey(1) & 0xFF == ord('f'):
            break


start = time.perf_counter()
LoadImages()
print('start encoding... ')

import pickle



# to read
with open('EncodingImage.txt', 'rb') as file:
    Outlist = pickle.load(file)


if len(Names) != len(Outlist):
    print("It seems that you added or removed an image  ")
    print("Begin start new encoding... ,  it will take awhile ")
    print("Don't worry  it will load faster next time")
    Outlist = findEncoding(images)
    #to write
    with open('EncodingImage.txt', 'wb') as file:
        pickle.dump(Outlist, file)


print(len(Names))
print(len(Outlist))

finish = time.perf_counter()
print('encoding complete....')
print(f'Finished in {round(finish - start, 2)} second(s)')
# faceRecognition()

t1 = threading.Thread(target=show)
t2 = threading.Thread(target=faceRecognition)

t1.start()
t2.start()

t1.join()
t2.join()
