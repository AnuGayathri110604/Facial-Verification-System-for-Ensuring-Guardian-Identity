
import cv2
from simple_facerec import SimpleFacerec
import pyttsx3

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        text_speech=pyttsx3.init()
        #answer=input("Enter the String to convert to Txt to Speech: ")
        text_speech.say(name)
        text_speech.runAndWait()
        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_TRIPLEX , 1, (220,20,60), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (220,20,60), 4)
        #t = name
        #text_to_speech(t)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
