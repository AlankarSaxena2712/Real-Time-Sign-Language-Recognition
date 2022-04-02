import os
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# create datagen object
datagen = ImageDataGenerator(
    rotation_range=0,
    zoom_range=0,
    horizontal_flip=False,
    fill_mode='constant'
    )

# read your dataset and apply the datagen object to it
# dataset = []
# path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dataset')
path = "Dataset/Static-Words"
folders = ['Family', 'Father', 'Fine', 'Hungry', 'IHateYou', 'Key', 'Love', 'Mother', 'okay', 'Pray']


# folders = list(os.listdir(path))
# print(folders)
# count the number of images in the folders
# for folder in folders:
#     # print(folder)
#     folder_path = os.path.join(path, folder)
#     # print(folder_path)
#     images = os.listdir(folder_path)
#     if len(images) == 15:
#         print(folder)

for imageFolders in folders:
    dataset = []
    for imageFiles in os.listdir(os.path.join(path, imageFolders)):
        if imageFiles.endswith('.png'):
            img = cv2.imread(os.path.join(path, imageFolders, imageFiles))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (50, 50))
            # cv2.imshow('image', img)
            dataset.append(img)
# print(np.array(dataset).shape)
    # print(imageFolders, "has", len(dataset), "images")
    i = 0
    for batch in datagen.flow(
        np.array(dataset),
        batch_size=15,
        save_to_dir=os.path.join(path, imageFolders),
        save_prefix='aug',
        save_format='jpg'
    ):    
        i += 1
        if i > 1499:
            break
    print(imageFolders, "augmnetation is done")
print("Done")