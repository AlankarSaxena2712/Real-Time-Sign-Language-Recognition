import os
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# create datagen object
datagen = ImageDataGenerator(
    rotation_range=20,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=False,
    brightness_range=[0.5, 1.5],
    fill_mode='constant'
    )

# dataset = []
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dataset')
for imageFolders in os.listdir(path):
    dataset = []
    for imageFiles in os.listdir(os.path.join(path, imageFolders)):
        if imageFiles.endswith('.jpg'):
            img = cv2.imread(os.path.join(path, imageFolders, imageFiles))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (256, 256))
            # cv2.imshow('image', img)
            dataset.append(img)

    # print(imageFolders, "has", len(dataset), "images")
    i = 0
    for batch in datagen.flow(
        np.array(dataset),
        batch_size=16,
        save_to_dir=os.path.join(path, imageFolders),
        save_prefix='aug',
        save_format='jpg'):    
        i += 1
        if i > 65:
            break
    print(imageFolders, "augmnetation is done")
print("Done")