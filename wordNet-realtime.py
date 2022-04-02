import cv2
import numpy as np
import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from tensorflow.keras.preprocessing.image import img_to_array
# import pyttsx3

# load saved model from PC
model = tf.keras.models.load_model('models/wordsNet.h5')
print(model.summary())

'''
dict_labels = {
    'Bus':0,
    'CalmDown':1,
    'Car':2,
    'Church':3,
    'Family':4,
    'Father':5,
    'Fine':6,
    'Hungry':7,
    'IHateYou':8,
    'Key':9,
    'Love':10,
    'Mother':11,
    'Pray':12,
    'okay':13
}'''

# label Mapping
dict_labels = {
    0:'Bus',
    1:'CalmDown',
    2:'Car',
    3:'Church',
    4:'Family',
    5:'Father',
    6:'Fine',
    7:'Hungry',
    8:'IHateYou',
    9:'Key',
    10:'Love',
    11:'Mother',
    12:'Pray',
    13:'okay'
}

#initiating the video source, 0 for internal camera
cap = cv2.VideoCapture(0)
while(True):
    
    _ , frame = cap.read()
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 0, 255), 5) 
    #region of intrest
    roi = frame[100:300, 100:300]
    img = cv2.resize(roi, (50, 50))
    cv2.imshow('roi', roi)
    arr = []
    img = img_to_array(img)
    arr.append(img)
    arr = np.array(arr)

    #make predication about the current frame
    prediction = model.predict(arr)
    label = np.argmax(prediction, axis=1)[0]
    # print(type(label))
    #print(char_index,prediction[0,char_index]*100)

    confidence = round(prediction[0,label]*100, 1)

    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale = 1
    color = (0,255,255)
    thickness = 2

    #writing the predicted char and its confidence percentage to the frame
    msg = dict_labels[label] + ', Conf:' + str(confidence) + '%'
    cv2.putText(frame, msg, (80, 80), font, fontScale, color, thickness)
    
    cv2.imshow('frame',frame)
    
    #close the camera when press 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
#release the camera and close all windows
cap.release()
cv2.destroyAllWindows()