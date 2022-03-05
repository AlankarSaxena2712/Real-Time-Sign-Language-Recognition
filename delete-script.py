import os

# datasetPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dataset')
# print(datasetPath)
datasetPath = r"D:\Projects\Real-Time-Sign-Language-Recognition"
folders = ['hello', 'ILoveYou', 'no', 'ThankYou', 'yes']
for imageFolders in folders:
    # print(imageFolders)
    for imageFiles in os.listdir(os.path.join(datasetPath, imageFolders)):
        # print(imageFiles)
        if imageFiles.startswith('aug'):
            # print(imageFiles)
            os.remove(os.path.join(datasetPath, imageFolders, imageFiles))
print('Done')