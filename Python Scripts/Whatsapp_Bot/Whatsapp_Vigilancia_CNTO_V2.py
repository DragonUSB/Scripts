import subprocess
import pyautogui as pg
import time
import webbrowser as web
import pandas as pd
from datetime import datetime

dia = datetime.today().weekday()
hora = datetime.today().hour
minuto = datetime.today().minute

semana = pd.read_csv('Python Scripts\Whatsapp_Bot\Cronograma_Vigilancia.csv', sep = ';')
telefonos = pd.read_csv('Python Scripts\Whatsapp_Bot\Telefonos.csv', sep = ';')
recibe = semana['RECIBE'][dia]
entrega = semana['ENTREGA'][dia]

for i in range(9):
    if telefonos['Personal'][i] == recibe:
        phone_recibe = '+58' + str(telefonos['Telefono'][i])
    if telefonos['Personal'][i] == entrega:
        phone_entrega = '+58' + str(telefonos['Telefono'][i])

print(phone_recibe)
print(phone_entrega)

# while True:
#     if hora == 14 and minuto == 30:
#         if dia < 4:
#             time.sleep(15)
#             mensaje_recibe = 'Buenas tardes companero, se les informa que el dia de manana recibe las llaves al vigilante del CNTO.'
#             web.open('https://api.whatsapp.com/send?phone=' + phone_recibe + '&text=' + mensaje_recibe)
#             time.sleep(15)
#             pg.press('enter')

#             time.sleep(15)
#             mensaje_entrega = 'Buenas tardes companero, se les informa que el dia de manana entrega las llaves al vigilante del CNTO.'
#             web.open('https://api.whatsapp.com/send?phone=' + phone_entrega + '&text=' + mensaje_entrega)
#             time.sleep(15)
#             pg.press('enter')
#         else:
#             time.sleep(15)
#             mensaje_recibe = 'Buenas tardes companero, se les informa que el dia Lunes recibe las llaves al vigilante del CNTO.'
#             web.open('https://api.whatsapp.com/send?phone=' + phone_recibe + '&text=' + mensaje_recibe)
#             time.sleep(15)
#             pg.press('enter')

#             time.sleep(15)
#             mensaje_entrega = 'Buenas tardes companero, se les informa que el dia Lunes entrega las llaves al vigilante del CNTO.'
#             web.open('https://api.whatsapp.com/send?phone=' + phone_entrega + '&text=' + mensaje_entrega)
#             time.sleep(15)
#             pg.press('enter')
#         break
#     hora = datetime.today().hour
#     minuto = datetime.today().minute

# subprocess.run('shutdown /s /f /t 1800')
# time.sleep(15)
# pg.press('enter')