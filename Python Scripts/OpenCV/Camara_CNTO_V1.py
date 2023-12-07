import cv2

cap = cv2.VideoCapture("rtsp://888888:888888@10.10.10.16:554/cam/realmonitor?channel=5")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('Camara 2', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()