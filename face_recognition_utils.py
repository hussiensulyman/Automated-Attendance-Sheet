import cv2
import numpy as np
import face_recognition
import os
import pickle
from class_names import class_names  # Directly import class_names

ENCODINGS_FILE = 'face_encodings.pickle'


def load_known_data():
    # Load known face encodings
    with open(ENCODINGS_FILE, 'rb') as file:
        known_face_encodings = pickle.load(file)

    return known_face_encodings, class_names


known_face_encodings, class_names = load_known_data()


def recognize_face(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    name_list= []

    face_locations = face_recognition.face_locations(image_rgb)
    face_encodings = face_recognition.face_encodings(image_rgb, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = class_names[best_match_index]
            name_list.append(name)

    return name_list