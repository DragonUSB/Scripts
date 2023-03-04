import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
placa = []

image = cv2.imread('OpenCV/Nueva-Placa.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray,(3,3))
canny = cv2.Canny(gray,150,200)
canny = cv2.dilate(canny,None,iterations=1)

#_,cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image,cnts,-1,(0,255,0),1)

for c in cnts:
  area = cv2.contourArea(c)

  x,y,w,h = cv2.boundingRect(c)
  epsilon = 0.09*cv2.arcLength(c,True)
  approx = cv2.approxPolyDP(c,epsilon,True)
  
  if len(approx)==4 and area>75000:
    print('area=',area)
    #cv2.drawContours(image,[approx],0,(0,255,0),3)

    aspect_ratio = float(w)/h
    if aspect_ratio>2:
      placa = gray[y+45:y+h-50,x+25:x+w-25]
      text = pytesseract.image_to_string(placa,config='--psm 11')
      print('PLACA: ',text)

      cv2.imshow('PLACA',placa)
      cv2.moveWindow('PLACA',800,10)
      cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
      cv2.putText(image,text,(x-20,y-10),1,2.2,(0,255,0),2)
      
cv2.imshow('Image',image)
cv2.moveWindow('Image',45,10)
cv2.waitKey(0)