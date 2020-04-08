import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime

import cv2
import numpy as np

face_cascade_path = 'C:\\data\\haarcascade_frontalface_default.xml'
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('カメラ無し')
    sys.exit()

while(True):
    bret, frame = cap.read()

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_rect = face_cascade.detectMultiScale(
        gray_img,
        scaleFactor= 1.05,
        minNeighbors= 8,
        minSize=(100,100)
        )

    for x,y,w,h in face_rect:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 1)

    cv2.imshow('camera', frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        date = datetime.now().strftime('%Y%m%d_%H%M%S')
        img_fn = date + '.png'
        cv2.imwrite(img_fn, frame)

cap.release()
cv2.destroyAllWindows()