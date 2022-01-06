# import the necessary packages
import cv2
import os
import numpy as np
import time

imageFolderPath = r"D:\Projects\Real-Time-Sign-Language-Recognition"

labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numberImgs = 20

for label in labels:
    cap = cv2.VideoCapture(0)
    print("Capturing images for", label)
    for i in range(numberImgs):
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(os.path.join(imageFolderPath, label, "img" + str(i) + ".jpg"), frame)
        else:
            print("Error capturing image")
        cv2.imshow("Capturing", frame)
        
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print("change the sign now!")
    time.sleep(5)
    cap.release()