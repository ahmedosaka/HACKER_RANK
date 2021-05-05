import cv2

#0 is black and white
#-1 is original and 1 is colored. not sure. search about it.
img = cv2.imread('assets/animegirl.jpg',0 )

#change size of the image
# img = cv2.resize(img,(0,0), fx=0.5, fy=0.3)
#rotate the image
# img= cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

#export the image
cv2.imwrite('assets/blackandwhiteanimegirl.jpg', img) 

#show image
cv2.imshow('Image', img)
#0 is wait forever, 1 is for 1 sec .. etc. 
#this function is meant to wait for you to press any key
cv2.waitKey(0)
#this is to close any open windows
cv2.destroyAllWindows()
