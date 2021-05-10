# import numpy as np
# import cv2
# from matplotlib import pyplot as plt

# img = cv2.imread('coins.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# cv2.imshow('img',thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('coins.jpg')
# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0
markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

