import cv2

cap = []
for i in range(1,6):
    cap.append(cv2.VideoCapture("rtsp://888888:888888@10.10.10.16:554/cam/realmonitor?channel=" + str(i)))

video = []
while True:
    for i in range(5):
        video.append(cap[i].read())
    frame = cv2.hconcat([video[0][1], video[1][1], video[2][1], video[3][1], video[4][1]])
    cv2.imshow('Camaras del CNTO', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()