import cv2
import numpy as np

imagen = cv2.imread('OpenCV/gato.jpeg')

cv2.circle(imagen, (40, 33), 7, (255,0,0), 2)
cv2.circle(imagen, (469, 41), 7, (0,255,0), 2)
cv2.circle(imagen, (69, 322), 7, (0,0,255), 2)
cv2.circle(imagen, (498, 330), 7, (255,255,0), 2)
    
pts1 = np.float32([[40,33], [469,41], [69, 322], [498,330]])
pts2 = np.float32([[0,0], [480,0], [0,300], [480,300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(imagen, M, (480,300))

cv2.imshow('Imagen', imagen)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()