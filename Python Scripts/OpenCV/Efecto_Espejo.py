import cv2

imagen = cv2.imread('OpenCV\Ave.jpg')
flip_1 = cv2.flip(imagen,10)

cv2.startWindowThread()
cv2.imshow('flip_1',flip_1)
cv2.waitKey(0)

'''
flip2 = cv2.flip(imagen,1)
flip3 = cv2.flip(imagen,-1)
cv2.imwrite('flip0.png',flip1)
cv2.imwrite('flip1.png',flip2)
cv2.imwrite('flip-1.png',flip3)
'''