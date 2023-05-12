import cv2
face = cv2.CascadeClassifier('venv/res/haarcascade_frontalface_alt2.xml')
cape = cv2.VideoCapture('venv/res/1080p.mp4')
while True:
  _, img = cape.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face.detectMultiScale(gray, 1.1, 2)
  for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 5)
  cv2.imshow("video", img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cape.release()
cv2.destroyAllWindows()
