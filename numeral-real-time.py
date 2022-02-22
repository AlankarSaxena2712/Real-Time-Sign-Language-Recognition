import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from tensorflow.keras.preprocessing.image import img_to_array
# import pyttsx3

# load saved model from PC
model = tf.keras.models.load_model('numeral_model.h5')
print(model.summary())

#initiating the video source, 0 for internal camera
cap = cv2.VideoCapture(0)
while(True):
    
    _ , frame = cap.read()
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 0, 255), 5) 
    #region of intrest
    roi = frame[100:300, 100:300]
    img = cv2.resize(roi, (128, 128))
    cv2.imshow('roi', roi)
    arr = []
    img = img_to_array(img)
    arr.append(img)
    arr = np.array(arr)

    #make predication about the current frame
    prediction = model.predict(arr)
    label = np.argmax(prediction, axis=1)
    #print(char_index,prediction[0,char_index]*100)

    # confidence = prediction[label]*100

    # Initialize the engine 
    # engine = pyttsx3.init() 
    # engine.say(label) 
    # engine.runAndWait()

    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 1
    color = (0,255,255)
    thickness = 2

    #writing the predicted char and its confidence percentage to the frame
    msg = str(label)
    cv2.putText(frame, msg, (80, 80), font, fontScale, color, thickness)
    
    cv2.imshow('frame',frame)
    
    #close the camera when press 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
#release the camera and close all windows
cap.release()
cv2.destroyAllWindows()