import cv2
import time
import numpy as np
 
vehicle_count=0;
car_classifier = cv2.CascadeClassifier(r"C:\Users\kashish\OneDrive\Desktop\Makeathon\OpenCV\haarcascade_car.xml")
cap = cv2.VideoCapture(r"C:\Users\kashish\OneDrive\Desktop\Makeathon\OpenCV\Vehicle-count-detect-main\Data\Cars.avi")
cap
while cap.isOpened():
    
    time.sleep(.05)
    # Read first frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    # Pass frame to our car classifier
    cars = car_classifier.detectMultiScale(gray, 1.4, 2)

    
    # Extract bounding boxes for any bodies identified
for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Cars', frame)


if cv2.waitKey(1) ==13: 
    raise Exception ('String Length is Not Equal')
      
cap.release()
cv2.destroyAllWindows()
