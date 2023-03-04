import pyautogui as pt
import pyperclip as pc
import datetime
from pynput.mouse import Controller, Button
from pynput.keyboard import Key, Controller
from time import sleep

# Requires opencv-python package for image recognition confidence

mouse = Controller()
keyboard = Controller()

hoy = datetime.datetime.now()

mensaje = open('texto2.txt')
mensaje = mensaje.readlines()
for linea in mensaje:
    print(linea)

class WhatsApp:

    # Defines the starting values
    def __init__(self, speed=.4, click_speed=.2):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    # Navigate to the logo
    def nav_logo(self):
        try:
            position = pt.locateOnScreen('logo.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(20, 20, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_logo): ', e)
    
    # Navigate to the lupa
    def nav_lupa(self):
        try:
            position = pt.locateOnScreen('lupa.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 20, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_lupa): ', e)
    
    # Search to contac
    def src_contac(self, contacto):
        try:
            pt.typewrite(contacto, interval=.1)
            pt.typewrite('\n')
        except Exception as e:
            print('Exception (src_contac): ', e)
    
    # Navigate to our message input box
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100, 10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box): ', e)
    
    # Sends the message to the user
    def send_message(self):
        try:
            pt.typewrite('Hola.', interval=.1)
            with keyboard.pressed(Key.ctrl):
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            pt.typewrite(f'Hoy es *{hoy.strftime("%d/%m/%Y")}*', interval=.1)
            pt.typewrite('\n')  # Sends the message (Disable it while testing)

        except Exception as e:
            print('Exception (send_message): ', e)

# Initialises the WhatsApp Bot
wa_bot = WhatsApp(speed=.5, click_speed=.4)

# Run the programme
contactos = ['rearmeca', 'elizabeth zerpa']
for contacto in contactos:
    if hoy.weekday() == 3 or hoy.weekday() == 2 or hoy.weekday() == 4:
        wa_bot.nav_logo()
        wa_bot.nav_lupa()
        wa_bot.src_contac(contacto)
        wa_bot.nav_input_box()
        wa_bot.send_message()

