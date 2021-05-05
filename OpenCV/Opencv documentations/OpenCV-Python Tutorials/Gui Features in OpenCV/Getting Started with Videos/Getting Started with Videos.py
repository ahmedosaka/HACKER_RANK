# import numpy as np
# import cv2

# cap = cv2.VideoCapture(0)

# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()


# https://dl172.iijjii.biz/?file=M3R4SUNiN3JsOHJ6WWQ3aTdPRFA4NW1rRVJIOHR2Y3RuY0J4akZVR1V1NFU5TWgzajZHRmNJd1hmT0pYNzgrSFFwc01wSHY1VkpXdVkwclI1OTErRURha3BKTmw2SHJ1cThWcmJlRlVIVERScWRXWDNRVlhvaUxLYUkrZlJZZ1lZR2N2NVVacTN5T3MzUERBc1VpOTRWdTBxRmlYZVNZUDkya3RNT1dFdE0xdWdDeVpTZTYyM3BFUnFHaWM3WmNDbDd1Y3NBanoxbzBxc05sS1dFMW1ZSVJpelp2KzJzL0NzRzR6bzY4TndGbXFqTjJ3VWN4bExPdVRhV00yT1NjR3RNWGZHaDRHM3l3TS9YaTMrNnA0dnpaYklmRW11RFBpcjdUNmNHS0xhSkU9

# import numpy as np
# import cv2

# cap = cv2.VideoCapture('https://dl172.iijjii.biz/?file=M3R4SUNiN3JsOHJ6WWQ3aTdPRFA4NW1rRVJIOHR2Y3RuY0J4akZVR1V1NFU5TWgzajZHRmNJd1hmT0pYNzgrSFFwc01wSHY1VkpXdVkwclI1OTErRURha3BKTmw2SHJ1cThWcmJlRlVIVERScWRXWDNRVlhvaUxLYUkrZlJZZ1lZR2N2NVVacTN5T3MzUERBc1VpOTRWdTBxRmlYZVNZUDkya3RNT1dFdE0xdWdDeVpTZTYyM3BFUnFHaWM3WmNDbDd1Y3NBanoxbzBxc05sS1dFMW1ZSVJpelp2KzJzL0NzRzR6bzY4TndGbXFqTjJ3VWN4bExPdVRhV00yT1NjR3RNWGZHaDRHM3l3TS9YaTMrNnA0dnpaYklmRW11RFBpcjdUNmNHS0xhSkU9')

# while(cap.isOpened()):
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()


# cv2.destroyAllWindows()


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()