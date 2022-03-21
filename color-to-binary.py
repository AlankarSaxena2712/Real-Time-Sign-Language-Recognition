import cv2
img = cv2.imread('aug_0_0.jpg')
img = cv2.resize(img, (500, 500))
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

tresh = 128
img_binary = cv2.threshold(img_grey, tresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('window', img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()