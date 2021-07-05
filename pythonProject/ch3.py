import cv2
import numpy as np

img = cv2.imread("D:\dahab\dahab1\IMG_20200131_142814.jpg")
print(img.shape)

imgResize = cv2.resize(img,(300,200))
imgcanny = cv2.Canny(imgResize,100,100)

imgCropped = imgResize[0:200 , 50:200]

cv2.imshow("img",imgResize)
cv2.imshow("sss",imgCropped)

cv2.waitKey(0)