import cv2
import face_recognition
 
imgAhmed = face_recognition.load_image_file('ImagesBasic/ahmed-cam.jpg')
imgAhmed = cv2.cvtColor(imgAhmed,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/ahmed.JPG')
if imgTest.shape[0] >800:
    imgTest = cv2.resize(imgTest, (0,0), dst=None,fx=0.3,fy=0.3)
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgAhmed)[0]
encodeAhmed = face_recognition.face_encodings(imgAhmed)[0]
cv2.rectangle(imgAhmed,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
 

results = face_recognition.compare_faces([encodeAhmed],encodeTest)
faceDis = face_recognition.face_distance([encodeAhmed],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
 
cv2.imshow('Ahmed',imgAhmed)
cv2.imshow('Elun',imgTest)
cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()