import numpy as np
import cv2
import random


img = cv2.imread('assets/animegirl.jpg')


tag = img[0:450,400:950]

cv2.imshow('Image', img)
cv2.imshow('tag', tag)
cv2.waitKey(0)
cv2.destroyAllWindows()
