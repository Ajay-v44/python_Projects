import face_recognitiion
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture=cv2.VideoCapture(0)

#load known images

rams_image=face_recognitiion.load_image_file("faces/ram.jpg")
ram_encoding=face_recognitiion.face_encodings(rams_image)[0]

known_face_encodings=[ram_encoding]
known_face_name=["ram"]
#list of expected students
students=known_face_name.copy()

face_location=[]
face_encodings=[]

#get the current date and time

now=datetime.now()
current_date=now.strftime('%Y-%m-%d')

f=open(f"{current_date}.csv","w+",newline="")
lnwriter=csv.writer((f))

while True:
    _,frame=video_capture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)

    #recognize faces
    face_locations=face_recognitiion.face_locations(rgb_small_frame)
    face_encodings=face_recognitiion.face_encodings(rgb_small_frame,face_locations)

    for face_encoding in face_encodings:
        matches=face_recognitiion.compare_faces(known_face_encodings,face_encoding)
        face_distance=face_recognitiion.face_distance(known_face_encodings)
        best_match_index=np.argmin(face_distance)
