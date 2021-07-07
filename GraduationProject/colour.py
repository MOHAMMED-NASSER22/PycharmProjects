from __future__ import division
import time
import cv2
import numpy as np



cap = cv2.VideoCapture(0)  # initiate camera capture

x_medium = 320  # detected line position
y_medium =240

while True:
    _, frame = cap.read()  # making copy of each frame
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # convert frame from RGB to HSV

    # selecting red color
    low_red = np.array([0, 114, 145])
    high_red = np.array([88, 197, 255])
    # selecting orange color
    low_orange = np.array([0, 174, 152])
    high_orange = np.array([179, 255, 255])
    # creating masks to isolate the prefered color
    orange_mask = cv2.inRange(hsv_frame, low_red, high_red)  # selected color is orange
    contours, _ = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    orange = cv2.bitwise_and(frame, frame, mask=orange_mask)

    # low = np.array([0, 42, 0])
    # high = np.array([179, 255, 255])
    # mask = cv2.inRange(hsv_frame, low, high)
    # R = cv2.bitwise_and(frame, frame, mask=mask)

    # draw a rectangular around the detected object
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # to drow rectangel
        x_medium = int((x + x + w) / 2)  # determine x center of rectangular
        y_medium = int((y + y + h) / 2)  # determine y center of rectangular

        break  # to exit the loop when the biggest value is detected

    cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)  # create line at the center of rectangular
    cv2.line(frame, (320, 0), (320, 480), (0, 255, 0), 2)  # create line at the center of frame

    cv2.line(frame, (0, y_medium), (640, y_medium), (0, 255, 0), 2)  # create line at the center of rectangular
    cv2.line(frame, (0, 240), (640, 240), (0, 255, 0), 2)  # create line at the center of frame

    x_destance = 320 - x_medium  # destance from the center of rectangular and the center of frame
    # print("xDestance = ", 320 - x_medium, "pos = ", position)  # testing print
    # print("yDestance = ", 320 - y_medium, "pos = ", position)  # testing print

    # cv2.imshow("red", orange)
    cv2.imshow("hopa", frame)  # show the frame
    # imgStack = stackImages(0.7,([orange,frame])) #calling the imgstack function to compine the mask and the frame
    # cv2.imshow("imgStack", imgStack) # show both the frame and the mask

    key = cv2.waitKey(1)

    if key == 27:  # closing all windows when esc is pressed
        break


cap.release()  # stop racording frame
cv2.destroyAllWindows()  # close all windows

