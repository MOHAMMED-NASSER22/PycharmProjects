import cv2
import numpy as np
import face_recognition
import os
import dlib
import time

start = time.perf_counter()

print('load complete....')

# imgElon = face_recognition.load_image_file('ImageBasic/Elon_Musk.jpg')
imgTest = face_recognition.load_image_file('ImageBasic/Elon_Musk3.jpg')
# imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
finish = time.perf_counter()
print(f'Finished load in {round(finish - start, 2)} second(s)')
start1 = time.perf_counter()
print('encoding complete....')

# faceLoc = face_recognition.face_locations(imgElon)[0]
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon, (faceLoc[3],faceLoc[0]), (faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

# result = face_recognition.compare_faces([encodeElon], encodeTest)
# faceDis = face_recognition.face_distance([encodeElon],encodeTest)
# print(result, faceDis)
# cv2.putText(imgTest,f'{result} {round(faceDis[0],2)}',(50,50) , cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2 )

finish1 = time.perf_counter()
print(f'Finished in {round(finish1 - start1, 2)} second(s)')

# cv2.imshow('elon', imgElon)
cv2.imshow('test', imgTest)
cv2.waitKey(0)
