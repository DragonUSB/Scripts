import time
import pyautogui as pg
import webbrowser as web
from pynput.mouse import Controller, Button
from pynput.keyboard import Key, Controller

mouse = Controller()
keyboard = Controller()

web.open('https://web.whatsapp.com/')
time.sleep(15)
pg.moveTo(-1500, 200)
pg.click()
pg.write('CNTO')
pg.press('enter')
time.sleep(15)
pg.write('Buen provecho')
pg.press('enter')