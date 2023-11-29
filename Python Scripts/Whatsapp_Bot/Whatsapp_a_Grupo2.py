import pyautogui as pg
import time
from selenium import webdriver
from pynput.mouse import Controller, Button
from pynput.keyboard import Key, Controller

ID_GROUP = "F2UGqRuOOfi8EhYuz8z8mE"

mouse = Controller()
keyboard = Controller()

driver = webdriver.Firefox()
driver.get('https://chat.whatsapp.com/' + ID_GROUP)

unirme = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div/div[2]/a[2]/span')
unirme.click()

pg.press('tab')
pg.press('tab')
pg.press('enter')

time.sleep(10)
pg.moveTo(1, 1)
pg.move(750, 700)
pg.click(button='left')

mensaje = open('Python Scripts\Whatsapp_Bot\Aviso_Cronograma_Vigilante.txt','r')
mensaje = mensaje.readlines()
print(mensaje[0] + mensaje[1] + mensaje[2] + mensaje[3])

time.sleep(10)
# pg.write(mensaje)
# pg.press('enter')
