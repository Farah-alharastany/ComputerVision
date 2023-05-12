import cv2
cap = cv2.VideoCapture(0)

#set the width, 3 is the ID of the width
cap.set(3, 640)
#set the highet, 4 is the ID of the highet
cap.set(4, 480)
#set the brightness, 10 is the ID of the brightness
cap.set(10, 100)
while True:
    success, img =  cap.read()
    cv2.imshow("webcam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break