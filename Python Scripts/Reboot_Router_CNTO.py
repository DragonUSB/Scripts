import pyautogui as pt
from selenium import webdriver
from pynput.mouse import Controller, Button
from pynput.keyboard import Key, Controller

mouse = Controller()
keyboard = Controller()

driver = webdriver.Firefox()
driver.get('http://10.10.0.1')

administration = driver.find_element('xpath', '/html/body/div/div/div[1]/div[2]/div/ul/li[7]/a')
administration.click()

pt.typewrite('Admin')
keyboard.press(Key.tab)
keyboard.release(Key.tab)
pt.typewrite('C1d4Cnt0W1f1')
keyboard.press(Key.enter)
keyboard.release(Key.enter)

driver.implicitly_wait(60)

reboot_btn = driver.find_element('xpath', '/html/body/div/div/div[2]/div/form/div/input[4]')
reboot_btn.click()

driver.implicitly_wait(60)

driver.quit()