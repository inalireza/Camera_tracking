# Import Neded Libray
import cv2  
from random import randrange
# Import Face Read Data as Xml File 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# Load Webcam
wbcam = cv2.VideoCapture(0)
# Make Loop For Play Frame per Frame Webcam
while True:
    #Set An LOad Fream in tabe
    successful_frame_read, frame = wbcam.read()

    # Change Image Color To BlacandWite (Gray)
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Make Line IN Arund Face In Video
    face_cordimtes = trained_face_data.detectMultiScale(grayscaled_img)
    #Past Line from xml data in arund face
    for (x, y, w, h) in face_cordimtes:# get x AND Y
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Make Des Window Frame For Show 
    cv2.imshow('Claver Progarm', frame)
    # Set key rfresh ( if (0) ined pushh key  in board to rfresh but (1) Refreshed pre second )
    key = cv2.waitKey(1)
    # set Q key in Keyboard For Exit And Break (With Ascci Code Q )
    if key==81 or key==113:
        break
print("End Face Detected SoftWear")
