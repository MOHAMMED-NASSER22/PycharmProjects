import cv2
import numpy as np

img = np.zeros((512,512,3))

#img[:]= 0,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),10)
cv2.rectangle(img, (0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(250,250,0),5)
cv2.putText(img , "OPEN", (300,200),cv2.FONT_ITALIC ,2,(0,150,0),5)
cv2.imshow("image", img)

cv2.waitKey(0)