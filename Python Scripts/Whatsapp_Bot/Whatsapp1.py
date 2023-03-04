import pyautogui as pg
import time
import webbrowser as web
phone_no="+584247585681"
parsedMessage="Mensaje De Prueba%0AMensaje De Prueba"
web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
pg.press('enter')
time.sleep(30)
for i in range(1):
    pg.write('We')
    pg.press('enter')
    print('Mensaje #'+str(i+1)+' enviado')
    pass
pg.alert('Bomba de mensajes finalizada')