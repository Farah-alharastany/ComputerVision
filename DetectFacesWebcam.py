import cv2
face = cv2.CascadeClassifier('venv/res/haarcascade_frontalface_alt2.xml')

#0 since we want the internl camera
camera = cv2.VideoCapture(0)

while(True):
    read_ok, frame = camera.read()
    labels = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
    faces = face.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+y, y+h), (0,0,255), 5)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
camera.release()
cv2.destroyAllWindows()