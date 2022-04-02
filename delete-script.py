import os

# datasetPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Dataset')
# print(datasetPath)
datasetPath = "Dataset/Static-Words"
folders = ['Bus', 'CalmDown', 'Car', 'Church', 'del', 'Family', 'Father', 'Fine', 'Hungry', 'IHateYou', 'Key', 'Love', 'Mother', 'okay', 'Pray']
for imageFolders in folders:
    # print(imageFolders)
    for imageFiles in os.listdir(os.path.join(datasetPath, imageFolders)):
        # print(imageFiles)
        if imageFiles.startswith('aug'):
            # print(imageFiles)
            os.remove(os.path.join(datasetPath, imageFolders, imageFiles))
print('Done')