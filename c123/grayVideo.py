import cv2

#Starting the camera
cap = cv2.VideoCapture(0)

while(True):
  # Capture frame-by-frame
    ret, frame = cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray Frame",gray)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()