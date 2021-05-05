# import numpy as np
# import cv2

# # Load an color image in grayscale
# # img = cv2.imread('assets\messi.jpg',0)
# # scale_percent =25  # percent of original size
# # width = int(img.shape[1] * scale_percent / 100)
# # height = int(img.shape[0] * scale_percent / 100)
# # dim = (width, height)
  
# # # resize image
# # resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# # cv2.imshow('image',resized)
# # cv2.imwrite('messigray.png',resized)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()



# img = cv2.imread('assets\messi.jpg',0)
# cv2.imshow('image',img)
# k = cv2.waitKey(0) & 0xFF
# if k == 27:         # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's' key to save and exit
#     cv2.imwrite('messigray.png',img)
#     cv2.destroyAllWindows()
    
    
    
    


# import numpy as np
# import cv2
# from matplotlib import pyplot as plt

# img = cv2.imread('assets\messi.jpg',-1)
# im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(im_rgb, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)