import pyautogui as pt
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.dateas.com/es/consulta_venezuela')

cedula = driver.find_element('xpath', '//*[@id="PERSON_venezuela_ci"]')
cedula.click()

pt.typewrite('14400419')

cedula = driver.find_element('xpath', '//*[@id="PERSON_submit"]')
cedula.click()

nombre = driver.find_element('xpath', '//*[@id="main-content"]/table[1]/tbody/tr[1]/td').text
print(nombre)

cedula = driver.find_element('xpath', '//*[@id="main-content"]/table[1]/tbody/tr[2]/td').text
print(cedula)

fecha = driver.find_element('xpath', '//*[@id="main-content"]/table[1]/tbody/tr[3]/td').text
print(fecha)

driver.implicitly_wait(60)

driver.quit()