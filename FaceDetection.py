import cv2 #import the library opencv

toLoadAlgorithnm = cv2.CascadeClassifier("Haarcascade/haarcascade_frontalface_default.xml")

image = cv2.imread("Fotos/imagem2.jpg")

#the algorithm read better when the image is gray

Grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#below do the face detection, after translate the image to "gray"

faces = toLoadAlgorithnm.detectMultiScale(Grayimage)

for (x,y,l,a) in faces: #here draw the rectangle in the faces
    cv2.rectangle(image,(x,y),(x+l,y+a),(0,255,0),2)
print(faces)

cv2.imshow("Face detection",image)#show the imagem
cv2.waitKey()