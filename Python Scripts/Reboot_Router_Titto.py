from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://4.4.4.1")

driver.implicitly_wait(10)

username = driver.find_element('name', 'loginUsername')
password = driver.find_element('name', 'loginPassword')

username.send_keys('admin')
password.send_keys('motorola')

login_btn = driver.find_element('xpath', '/html/body/table/tbody/tr[3]/td[2]/form/p/table/tbody/tr[3]/td/input')
login_btn.click()

driver.implicitly_wait(10)

configuration = driver.find_element('xpath', '/html/body/font/table/tbody/tr[3]/td[1]/p[5]/a/img')
configuration.click()

driver.implicitly_wait(10)

reboot = driver.find_element('xpath', '/html/body/font/table/tbody/tr[3]/td[2]/form/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input')
reboot.click()

driver.implicitly_wait(10)

driver.quit()