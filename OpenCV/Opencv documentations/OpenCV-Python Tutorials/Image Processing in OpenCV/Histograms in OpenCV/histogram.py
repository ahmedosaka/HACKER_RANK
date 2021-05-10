# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('Louane.jpg',0)
# plt.hist(img.ravel(),256,[0,256]); plt.show()


'''
Plotting Histograms
1. Using Matplotlib
'''
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('Louane.jpg')
# color = ('b','g','r')
# for i,col in enumerate(color):
#     histr = cv2.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(histr,color = col)
#     plt.xlim([0,256])
# plt.show()



'''
Plotting Histograms
Using OpenCV
Application of Mask
'''
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# img = cv2.imread('Louane.jpg',0)

# # create a mask
# mask = np.zeros(img.shape[:2], np.uint8)
# mask[50:500, 600:1150] = 255
# masked_img = cv2.bitwise_and(img,img,mask = mask)

# # Calculate histogram with mask and without mask
# # Check third argument for mask
# hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
# hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

# plt.subplot(221), plt.imshow(img, 'gray')
# plt.subplot(222), plt.imshow(mask,'gray')
# plt.subplot(223), plt.imshow(masked_img, 'gray')
# plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
# plt.xlim([0,256])

# plt.show()

# Histograms - 3 : 2D Histograms

# import cv2
# import numpy as np

# img = cv2.imread('home.jpg')
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Louane.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )

plt.imshow(hist,interpolation = 'nearest')
plt.show()