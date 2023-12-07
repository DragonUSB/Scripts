import cv2
import os
import platform

absolute_path = os.path.dirname(__file__)
sistema = platform.system()

if sistema == 'Linux':
    file = absolute_path + '/FigurasColores2.png'
else:
    file = absolute_path + '\FigurasColores2.png'

imagen = cv2.imread(file)
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#_,cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 3
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 4
#cv2.drawContours(imagen, cnts, -1, (0,255,0), 2)

for c in cnts:
	epsilon = 0.01*cv2.arcLength(c,True)
	approx = cv2.approxPolyDP(c,epsilon,True)
	#print(len(approx))
	x,y,w,h = cv2.boundingRect(approx)

	if len(approx)==3:
		cv2.putText(imagen,'Triangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==4:
		aspect_ratio = float(w)/h
		print('aspect_ratio= ', aspect_ratio)
		if aspect_ratio == 1:
			cv2.putText(imagen,'Cuadrado', (x,y-5),1,1,(0,255,0),1)
		else:
			cv2.putText(imagen,'Rectangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==5:
		cv2.putText(imagen,'Pentagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==6:
		cv2.putText(imagen,'Hexagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)>10:
		cv2.putText(imagen,'Circulo', (x,y-5),1,1,(0,255,0),1)

	cv2.drawContours(imagen, [approx], 0, (0,255,0),2)
	cv2.imshow('imagen',imagen)
	cv2.waitKey(0)