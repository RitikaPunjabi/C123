import cv2

#Starting the camera
cap = cv2.VideoCapture(0)

while(True):
  # Capture frame-by-frame
    ret, frame = cap.read()

    cv2.imshow("COlor Frame",frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()