import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('venv/res/img_3.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
plt.imshow(gray, cmap='gray')
plt.show()

def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)

face = cv2.CascadeClassifier('venv/res/haarcascade_frontalface_alt2.xml')
face_c = face.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=2)
print('Faces found: ', len(face_c))

for(x_face, y_face, w_face, h_face) in face_c:
    cv2.rectangle(image, (x_face, y_face), (x_face+w_face, y_face+h_face), (0,255,0),5)

plt.imshow(convertToRGB(image))
plt.show()
