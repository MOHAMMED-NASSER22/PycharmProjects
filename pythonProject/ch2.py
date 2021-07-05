import  cv2
import numpy as np

img = cv2.imread("D:\dahab\dahab1\IMG_20200131_142814.jpg")

imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
imgBlue = cv2.GaussianBlur(imgGray ,(7,7),1)
imgcanny = cv2.Canny(img,100,100)
imgDig = cv2.dilate(imgGray , kernel=.5 ,iterations= 1)

cv2.imshow("GRAY",imgGray)
cv2.imshow("Blur",imgBlue)
cv2.imshow("cany",imgcanny)
cv2.imshow("cany",imgDig)

cv2.waitKey(0)

