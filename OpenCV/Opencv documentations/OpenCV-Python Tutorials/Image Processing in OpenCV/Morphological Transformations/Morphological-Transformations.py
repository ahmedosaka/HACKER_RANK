# # 1. Erosion
# import cv2
# import numpy as np

# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(img,kernel,iterations = 1)

# cv2.imshow('img',erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 2. Dilation

# import cv2
# import numpy as np

# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# dilation = cv2.dilate(img,kernel,iterations = 1)

# cv2.imshow('img',dilation)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# # 3. Opening

# import cv2
# import numpy as np

# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# cv2.imshow('img',opening)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 4. Closing


# import cv2
# import numpy as np

# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# cv2.imshow('img',closing)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 5. Morphological Gradient
# import cv2
# import numpy as np

# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# cv2.imshow('img',gradient)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 6. Top Hat
# import cv2
# import numpy as np

# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# cv2.imshow('img',tophat)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 7. Black Hat

# import cv2
# import numpy as np

# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# cv2.imshow('img',blackhat)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# # Structuring Element

import cv2
import numpy as np

img = cv2.imread('j.png',0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('img',gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()