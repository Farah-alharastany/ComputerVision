import cv2
cap = cv2.VideoCapture("venv/res/vid.mp4")
while True:
    #sucess is a boolean variable, img will store the image captures
    success, img = cap.read()
    cv2.imshow("Vidoe", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break