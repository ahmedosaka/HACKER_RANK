import numpy as np
import cv2
import random

img = cv2.imread('assets/animegirl.jpg')

# print(img.shape[1])
'''
this code is to select the first 100 row and then
selecet all the columns and change all the values 
to a random colors.
for i in range(1): selected the first row
    for j in range(img.shape[1]): chooses all the columns
        img[i][j] = first rowm ,first column and then you 
        give a value of a list

'''
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255) ]


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()