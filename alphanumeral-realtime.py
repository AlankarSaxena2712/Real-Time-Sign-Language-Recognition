import cv2
import numpy as np
import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from tensorflow.keras.preprocessing.image import img_to_array
# import pyttsx3

# load saved model from PC
model = tf.keras.models.load_model('models/alphanumeralNet.h5')
print(model.summary())

# label Mapping
dict_labels = {
    1:'_',
    2:'0',
    3:'1',
    4:'2',
    5:'3',
    6:'4',
    7:'5',
    8:'6',
    9:'7',
    10:'8',
    11:'9',
    12:'A',
    13:'B',
    14:'C',
    15:'D',
    16:'E',
    17:'F',
    18:'G',
    19:'H',
    20:'I',
    21:'J',
    22:'K',
    23:'L',
    24:'M',
    25:'N',
    26:'O',
    27:'P',
    28:'Q',
    29:'R',
    30:'S',
    31:'T',
    32:'U',
    33:'V',
    34:'W',
    35:'X',
    36:'Y',
    37:'Z'
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