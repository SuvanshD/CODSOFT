### CODSOFT TASK-5 [Face Detection And Recognition Using pre-trained face detection models like Haarcascades] ###

import cv2
import time

# Load the pre-trained Haar Cascade face detection model
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the webcam
video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()
    print("Frame read status:", ret)
    
    if ret:
        dol = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
        faces = face_cap.detectMultiScale(
            dol,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50, 50),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        if len(faces) > 0:
            print("Face detected")
            for (x, y, w, h) in faces:
                cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Change color to red
        else:
            print("Face not recognized")
        
        cv2.imshow("video_live", video_data)
        if cv2.waitKey(10) & 0xFF == ord("a"):
            break
    else:
        print("Error reading frame")
    
    # Add a delay of 1 second
    time.sleep(0.3)

# Release video capture and close windows
video_cap.release()
cv2.destroyAllWindows()