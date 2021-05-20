import cv2
import numpy as np

img1 = cv2.imread('whiteBackGround.jpg')
img2 = cv2.imread('WhiteGirl.jpg')
# img2 = cv2.imread('black-backgrounded.jpg')

#resize image
# img2 = cv2.resize(img2, (0,0), fx=0.33, fy=0.33) 

rows, cols, channels = img2.shape
#region of interest
roi = img1[0:rows,0:cols]

img2gray= cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,235, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('whiteBackGround', img1)
cv2.imshow('Girl', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
