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
