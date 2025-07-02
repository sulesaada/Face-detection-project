import cv2

face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('WIN_20250702_14_53_53_Pro.jpg')

grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Grey", grey)

#cv2.waitKey(0)

faces = face_haar_cascade.detectMultiScale(grey, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
    
cv2.imshow("Faces", image)
cv2.waitKey(0)
