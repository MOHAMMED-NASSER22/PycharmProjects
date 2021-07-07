def FaceRec():
    import cv2
    import numpy as np
    import face_recognition
    import os
    import threading
    import time

    global  name_faceRec
    name_faceRec = 'unknown'
    global X_Center_faceRec
    X_Center_faceRec = 320
    global Y_Center_faceRec
    Y_Center_faceRec = 240
    global IsKnown_faceRec
    IsKnown_faceRec = False
    def config():
        print("reading ImageAt...")
        path = 'ImageAt'
        images = []
        Names = []
        X_Center_faceRec = 320
        Y_Center_faceRec = 240

        cap = cv2.VideoCapture(0)
        _, img = cap.read()
        _, imgS = cap.read()

        return img, imgS, images, Names, Y_Center_faceRec, X_Center_faceRec, path, cap

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

    def EncodingImage():
        import pickle

        # to read
        with open('EncodingImage.txt', 'rb') as file:
            Outlist = pickle.load(file)

        if len(Names) != len(Outlist):
            print("It seems that you added or removed an image  ")
            print("Begin start new encoding... ,  it will take awhile ")
            print("Don't worry  it will load faster next time")
            Outlist = findEncoding(images)
            # to write
            with open('EncodingImage.txt', 'wb') as file:
                pickle.dump(Outlist, file)
        return Outlist
        print(len(Names))
        print(len(Outlist))

    def LiveFeed():

        while True:
            try:  # there is many problem occur here from threading  exception  so i except the exception XD And it work !!!
                while True:
                    _, LiveFeed = cap.read()

                    if IsKnown_faceRec == True  :  # here we will move the motor
                        print(name_faceRec)
                        print(" X_Center :  " + str(X_Center_faceRec) + "  Y_Center :  " + str(Y_Center_faceRec))


                    cv2.imshow("LiveFeed", LiveFeed)
                    if cv2.waitKey(10) & 0xFF == ord('s'):
                        break





            except:
                print("there is something wrong happend in thread 1 ( LiveFeed ) , trying again ....")

    def faceRecognition():
        while True:
            try:  # there is many problem occur here from threading exception  so i except the exception XD And it work !!!

                global name_faceRec
                global X_Center_faceRec
                global Y_Center_faceRec
                global IsKnown_faceRec
                # global facesCurFrame

                while True:
                    time.sleep(1)
                    _, imgS = cap.read()
                    # _, img = cap.read()

                    #
                    # _, imgS = cap.read()
                    # _, imgS = cap.read()
                    # imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
                    imgSGRAY = cv2.cvtColor(imgS, cv2.COLOR_BGR2GRAY)
                    imgSRGB = cv2.cvtColor(imgSGRAY, cv2.COLOR_BGR2RGB)

                    facesCurFrame = face_recognition.face_locations(imgSRGB)
                    # print(facesCurFrame)
                    encodesCurFrame = face_recognition.face_encodings(imgSRGB, facesCurFrame)

                    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                        matches = face_recognition.compare_faces(Outlist, encodeFace)
                        # print(matches)
                        faceDis = face_recognition.face_distance(Outlist, encodeFace)
                        # print(faceDis)
                        matchIndex = np.argmin(faceDis)
                        # print(matchIndex)
                        # print(matches[matchIndex])
                        IsKnown_faceRec = matches[matchIndex]  # there is no known face
                        if matches[matchIndex]:
                            # IsKnown_faceRec = True  # there is known face
                            name_faceRec = Names[matchIndex].upper()
                            # print(name_faceRec)
                            y1, x2, y2, x1 = faceLoc
                            # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                            cv2.rectangle(imgS, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            # cv2.rectangle(imgS, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                            cv2.putText(imgS, name_faceRec, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 2)
                            # cv2.putText(imgS, f'{name_faceRec} {round(1 - (faceDis[matchIndex]), 2)}', (x1 + 6, y2 - 6),
                            #             cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255),
                            #             2)  # if i want to print the matches percent %
                            # markAttendce(name_faceRec)
                            # faceloc1 = faceLoc
                            X_Center_faceRec = (x1 + x2) / 2
                            Y_Center_faceRec = (y1 + y2) / 2
                            # IsKnown_faceRec = False
                        else:
                            name_faceRec = 'UNKNOWN'
                            print(name_faceRec)
                            y1, x2, y2, x1 = faceLoc
                            # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                            cv2.rectangle(imgS, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            # cv2.rectangle(imgS, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                            cv2.putText(imgS, name_faceRec, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, .9, (255, 255, 255), 2)

                    cv2.imshow('faceRecognition', imgS)
                    if cv2.waitKey(1) & 0xFF == ord('f'):
                        break

            except:
                print("there is something wrong happend in thread 2 ( faceRecognition ) , trying again ....")

    def finaly():
        start = time.perf_counter()
        LoadImages()
        print('start encoding... ')
        Outlist = EncodingImage()
        finish = time.perf_counter()
        print('encoding complete....')
        print(f'Finished in {round(finish - start, 2)} second(s)')

        return Outlist

    img, imgS, images, Names, Y_Center_faceRec, X_Center_faceRec, path, cap = config()
    Outlist = finaly()

    # threading
    t1 = threading.Thread(target=LiveFeed)  # Thread 1
    t2 = threading.Thread(target=faceRecognition)  # Thread 2
    t1.start()
    t2.start()
    t1.join()
    t2.join()




FaceRec()
