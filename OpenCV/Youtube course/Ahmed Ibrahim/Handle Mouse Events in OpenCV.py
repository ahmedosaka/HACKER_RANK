# #the following code will print an image and with left click will show you the color and with right click will show you the location of the
# #pixel

# import numpy as np
# import cv2

# events = [i for i in dir(cv2) if 'EVENT' in  i]
# print(events)

# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x,', ' ,y)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         strXY = str(x) + ', '+ str(y)
#         cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
#         cv2.imshow('image', img)
#     if event == cv2.EVENT_RBUTTONDOWN:
#         blue = img[y, x, 0]
#         green = img[y, x, 1]
#         red = img[y, x, 2]
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
#         cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
#         cv2.imshow('image', img)

# #img = np.zeros((512, 512, 3), np.uint8)
# img = cv2.imread('fish.jpg')
# cv2.imshow('image', img)

# cv2.setMouseCallback('image', click_event)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




# #This code will draw a point and a line connecting the 2 points 
# #you will draw. Run to check.
# import numpy as np
# import cv2

# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img,(x,y),13,(255,0,0),-1)
#         points.append((x,y))
#         if len(points)>=2:
#             cv2.line(img, points[-1], points[-2],(0,255,255))
            
#         cv2.imshow('image', img)
# img = np.zeros((512,512,3), np.uint8)
# #img = np.zeros((512, 512, 3), np.uint8)
# cv2.imshow('image', img)

# points=[]

# cv2.setMouseCallback('image', click_event)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# this code shows the selected color by clicking on it in a new window.
import numpy as np
import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        mycolorimage= np.zeros((512,512,3),dtype = np.uint8)
        mycolorimage[:]=[ blue ,green, red]
    
        

        cv2.imshow('color', mycolorimage)
    

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('fish.jpg')
cv2.imshow('image', img)


cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()