import pyautogui as pg
import time
import webbrowser as web

time.sleep(5)

# f = open('Python Scripts\Whatsapp_Bot\Texto2.txt','r')
# f = f.read()
# print(f)

phone_no = "+584161156701"
mensaje_recibe = 'Buenas tardes companero, se les informa que el dia de manana recibe las llaves al vigilante del CNTO.'
mensaje_entrega = 'Buenas tardes companero, se les informa que el dia de manana recibe y entrega las llaves al vigilante del CNTO el siguiente personal.'
web.open('https://api.whatsapp.com/send?phone=' + phone_no + '&text=' + mensajeentrega)
time.sleep(5)
pg.press('enter')

print("Mensaje Enviado")
