<<<<<<< HEAD
import dlib
import cv2
#http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
face_detector = dlib.get_frontal_face_detector()
landmark_detector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
img_path = "ImageAt/M_Nasser.jpg"
# read with dlib
img = dlib.load_rgb_image(img_path)
# read with opencv
# img = cv2.imread(img_path)[:,:,::-1]
faces = face_detector(img, 1)
landmark_tuple = []
for k, d in enumerate(faces):
   landmarks = landmark_detector(img, d)
   for n in range(37, 48): # Here u choose the set of landmark [0: 68] look to the Graduation Book in (1.7.2 Dlib) for more explantion
      x = landmarks.part(n).x       # link for the book : https://docs.google.com/document/d/12WatTbiF8Bi39qQ0UjLxNVjV_Na0xiySEOkOXtHfITQ/
      y = landmarks.part(n).y
      landmark_tuple.append((x, y))
      cv2.circle(img, (x, y), 2, (255, 255, 0), -1)
while True :
    cv2.imshow("show" , img)
    if cv2.waitKey(10) & 0xff == ord("s"):
=======
import dlib
import cv2
#http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
face_detector = dlib.get_frontal_face_detector()
landmark_detector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
img_path = "ImageAt/M_Nasser.jpg"
# read with dlib
img = dlib.load_rgb_image(img_path)
# read with opencv
# img = cv2.imread(img_path)[:,:,::-1]
faces = face_detector(img, 1)
landmark_tuple = []
for k, d in enumerate(faces):
   landmarks = landmark_detector(img, d)
   for n in range(37, 48): # Here u choose the set of landmark [0: 68] look to the Graduation Book in (1.7.2 Dlib) for more explantion
      x = landmarks.part(n).x       # link for the book : https://docs.google.com/document/d/12WatTbiF8Bi39qQ0UjLxNVjV_Na0xiySEOkOXtHfITQ/
      y = landmarks.part(n).y
      landmark_tuple.append((x, y))
      cv2.circle(img, (x, y), 2, (255, 255, 0), -1)
while True :
    cv2.imshow("show" , img)
    if cv2.waitKey(10) & 0xff == ord("s"):
>>>>>>> a179ab5e53b79f0490394e2a68598f09576a8464
        break