<<<<<<< HEAD
import cv2
import numpy as np
import face_recognition
import os
import dlib
import time

def stackImages(scale, imgArray):
    rows = len(imgArray)  # setting the rows
    cols = len(imgArray[0])  # setting the colums
    rowsAvailable = isinstance(imgArray[0], list)  # determinig available rows
    width = imgArray[0][0].shape[1]  # determining width
    height = imgArray[0][0].shape[0]  # determining height
    if rowsAvailable:  # checking for available rows
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

start = time.perf_counter()


print('loading Images....')
imgNasser = face_recognition.load_image_file('ImageBasic/M_Nasser.jpg')
imgTest = face_recognition.load_image_file('ImageBasic/M_Nasser2.png')
imgTest2 = face_recognition.load_image_file('ImageBasic/Elon_Musk.jpg')

imgNasser = cv2.cvtColor(imgNasser, cv2.COLOR_BGR2RGB)
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
imgTest2 = cv2.cvtColor(imgTest2, cv2.COLOR_BGR2RGB)
finish = time.perf_counter()
print(f'Finished load in {round(finish - start, 2)} second(s)')
start1 = time.perf_counter()
print('encoding complete....')

faceLoc = face_recognition.face_locations(imgNasser)[0]
encodeNasser = face_recognition.face_encodings(imgNasser)[0]
cv2.rectangle(imgNasser, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

faceLocTest2 = face_recognition.face_locations(imgTest2)[0]
encodeTest2 = face_recognition.face_encodings(imgTest2)[0]
cv2.rectangle(imgTest2, (faceLocTest2[3], faceLocTest2[0]), (faceLocTest2[1], faceLocTest2[2]), (255, 0, 255), 2)

result = face_recognition.compare_faces([encodeNasser], encodeTest)
faceDis = face_recognition.face_distance([encodeNasser], encodeTest)
cv2.putText(imgTest, f'{result} ', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

result2 = face_recognition.compare_faces([encodeNasser], encodeTest2)
faceDis2 = face_recognition.face_distance([encodeNasser], encodeTest2)
cv2.putText(imgTest2, f'{result2} ', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

finish1 = time.perf_counter()
print(f'Finished in {round(finish1 - start1, 2)} second(s)')

imgStack = stackImages(.5, ([imgNasser, imgTest], [imgNasser , imgTest2]))
cv2.imshow('FaceRecognition', imgStack)

cv2.waitKey(0)
=======
import cv2
import numpy as np
import face_recognition
import os
import dlib
import time

def stackImages(scale, imgArray):
    rows = len(imgArray)  # setting the rows
    cols = len(imgArray[0])  # setting the colums
    rowsAvailable = isinstance(imgArray[0], list)  # determinig available rows
    width = imgArray[0][0].shape[1]  # determining width
    height = imgArray[0][0].shape[0]  # determining height
    if rowsAvailable:  # checking for available rows
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

start = time.perf_counter()


print('loading Images....')
imgNasser = face_recognition.load_image_file('ImageBasic/M_Nasser.jpg')
imgTest = face_recognition.load_image_file('ImageBasic/M_Nasser2.png')
imgTest2 = face_recognition.load_image_file('ImageBasic/Elon_Musk.jpg')

imgNasser = cv2.cvtColor(imgNasser, cv2.COLOR_BGR2RGB)
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
imgTest2 = cv2.cvtColor(imgTest2, cv2.COLOR_BGR2RGB)
finish = time.perf_counter()
print(f'Finished load in {round(finish - start, 2)} second(s)')
start1 = time.perf_counter()
print('encoding complete....')

faceLoc = face_recognition.face_locations(imgNasser)[0]
encodeNasser = face_recognition.face_encodings(imgNasser)[0]
cv2.rectangle(imgNasser, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

faceLocTest2 = face_recognition.face_locations(imgTest2)[0]
encodeTest2 = face_recognition.face_encodings(imgTest2)[0]
cv2.rectangle(imgTest2, (faceLocTest2[3], faceLocTest2[0]), (faceLocTest2[1], faceLocTest2[2]), (255, 0, 255), 2)

result = face_recognition.compare_faces([encodeNasser], encodeTest)
faceDis = face_recognition.face_distance([encodeNasser], encodeTest)
cv2.putText(imgTest, f'{result} ', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

result2 = face_recognition.compare_faces([encodeNasser], encodeTest2)
faceDis2 = face_recognition.face_distance([encodeNasser], encodeTest2)
cv2.putText(imgTest2, f'{result2} ', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

finish1 = time.perf_counter()
print(f'Finished in {round(finish1 - start1, 2)} second(s)')

imgStack = stackImages(.5, ([imgNasser, imgTest], [imgNasser , imgTest2]))
cv2.imshow('FaceRecognition', imgStack)

cv2.waitKey(0)
>>>>>>> a179ab5e53b79f0490394e2a68598f09576a8464
