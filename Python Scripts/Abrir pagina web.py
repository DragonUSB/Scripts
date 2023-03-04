import webbrowser
webbrowser.open("http://4.4.4.1", new=2, autoraise=True)

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://4.4.4.1")