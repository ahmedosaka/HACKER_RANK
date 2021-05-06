import cv2
import numpy as np

img = cv2.imread('messi.jpg')
img = cv2.resize(img, None, fx = 0.25, fy = 0.25)

# px = img[100,100]
# print(px)

# # accessing only blue pixel
# blue = img[100,100,0]
# print(blue)


# img[100,100] = [255,255,255]
# print (img[100,100])


# # accessing RED value
# img.item(10,10,2)


# # modifying RED value
# img.itemset((10,10,2),100)
# print(img.item(10,10,2))

# print (img.shape)


# print (img.size)



# print (img.dtype)


# # print (img.size)


# ball = img[1738:1414, 1976:1636]
# print(ball.shape)

# img[273:333, 100:160] = ball
# twiceImg = cv2.resize(img, None, fx = 0.25, fy = 0.25)

# cv2.imshow('image',twiceImg)
# k = cv2.waitKey(0) & 0xFF
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()


# b,g,r = cv2.split(img)
# img = cv2.merge((b,g,r))
# b = img[:,:]

# cv2.imshow('image',b)
# k = cv2.waitKey(0) & 0xFF
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()



import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = img #cv2.imread('opencv-logo-white.png')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()