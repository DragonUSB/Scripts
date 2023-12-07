import cv2

cap = []
for i in range(1,6):
    cap.append(cv2.VideoCapture("rtsp://888888:888888@10.10.10.16:554/cam/realmonitor?channel=" + str(i)))

video = []
while True:
    for i in range(5):
        video.append(cap[i].read())
    # frame = cv2.hconcat([video[0][1], video[1][1], video[2][1], video[3][1], video[4][1]])
    
    if video[0][0]:
        cv2.imshow('Camara 1', video[0][1])
    
    if video[1][0]:
        cv2.imshow('Camara 2', video[1][1])
    
    if video[2][0]:
        cv2.imshow('Camara 3', video[2][1])
    
    if video[3][0]:
        cv2.imshow('Camara 4', video[3][1])
    
    if video[4][0]:
        cv2.imshow('Camara 5', video[4][1])
    
    # cv2.imshow('Camaras del CNTO', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap[0].release() 
cap[1].release()
cap[2].release()
cap[3].release()
cap[4].release()
cv2.destroyAllWindows()