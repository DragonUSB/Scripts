import pyautogui as pg
import time
import webbrowser as web

time.sleep(5);

f = open('Texto2.txt','r')
f = f.read()
print(f)

phone_no = "+584247585681"
parsedMessage = f
web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
pg.press('enter')
print("Mensaje Enviado")