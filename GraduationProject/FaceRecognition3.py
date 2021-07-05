import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import threading
import time
import multiprocessing
import concurrent.futures
import multiprocessing

print("reading ImageAt...")
path = 'ImageAt'
images = []
Names = []
cap = cv2.VideoCapture(0)



def LoadImages():
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        Names.append(os.path.splitext(cl)[0])
    print(Names)


def show():
    while True:
        _, img1 = cap.read()
        cv2.imshow("show", img1)
        if cv2.waitKey(10) & 0xFF == ord('s'):
            break


def findEncoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def faceRecognition():
    while True:
        time.sleep(1)
        _, img = cap.read()
        _ , imgS = cap.read()
        # imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        # imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2GRAY)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = Names[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
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
        if cv2.waitKey(1) & 0xFF == ord('f'):
            break


start = time.perf_counter()
LoadImages()
print('start encoding... ')
encodeListKnown = findEncoding(images)
finish = time.perf_counter()
print('encoding complete....')
print(f'Finished in {round(finish - start, 2)} second(s)')

# with concurrent.futures.ThreadPoolExecutor() as executer :
#     executer.submit(show)
#     executer.submit(faceRecognition)


# # multiprocessing
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=show)
#     p2 = multiprocessing.Process(target=faceRecognition)
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#     finish = time.perf_counter()
#
#     print(f'Finished in {round(finish - start, 2)} second(s)')

# threading
t1 = threading.Thread(target=show)
t2 = threading.Thread(target=faceRecognition)
t1.start()
t2.start()

t1.join()
t2.join()
