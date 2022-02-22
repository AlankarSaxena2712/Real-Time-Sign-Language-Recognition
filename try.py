import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

model = tf.keras.models.load_model('numeral_model.h5')

arr = []
path = r"D:\Projects\Real-Time-Sign-Language-Recognition\Dataset\Numerals\5\aug_0_1222.jpg"
img = load_img(path, target_size=(128, 128))
img = img_to_array(img)
img=img/255.0
arr.append(img)
arr = np.array(arr)
y = model.predict(arr)
print(y)
label = np.argmax(y, axis=1)
print(label)