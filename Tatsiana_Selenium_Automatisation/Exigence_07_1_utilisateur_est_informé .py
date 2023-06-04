# Precondition:
# Compte existe avec:
# first name = 'John'
# last name = 'Travolta'
# email: "jtravolta@rabah.com"

import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import datetime

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://tutorialsninja.com/demo/index.php?route=common/home")
driver.maximize_window()
time.sleep(1)

#Cliquer sur le lien My account
driver.find_element(By.XPATH,"//span[contains(text(),'My Account')]").click()
time.sleep(2)

email = 'jtravolta@rabah.com'
password = "password"
product = "Samsung"

# Cliquer sur le lien d'inscription
register_link = driver.find_element(By.XPATH,"//a[normalize-space()='Login']")
register_link.click()

driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys(email)
driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys(password)
driver.find_element(By.XPATH,"//input[@value='Login']").click()

driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@placeholder='Search']").is_displayed()
driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(product)
driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()

#Wait until the element is displayed
wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
driver.find_element(By.XPATH,"//h1[contains(text(),'Samsung')]").is_displayed()
driver.find_element(By.XPATH,"//div[@class='caption']//a[contains(text(),'Samsung SyncMaster 941BW')]").click()
driver.find_element(By.XPATH,"//button[@id='button-cart']").click()
driver.find_element(By.XPATH,"//span[@id='cart-total'][contains(text(),' 1 item(s) - $200.00')]").is_displayed()
driver.find_element(By.XPATH,"//span[@id='cart-total'][contains(text(),' 1 item(s) - $200.00')]").click()
driver.find_element(By.XPATH,"//p[@class='text-right']/a[2]//i").click()
driver.find_element(By.XPATH,"//input[@id='button-payment-address']").click()
driver.find_element(By.XPATH,"//input[@id='button-shipping-address']").click()
driver.find_element(By.XPATH,"//input[@id='button-shipping-method']").click()
driver.find_element(By.XPATH,"//input[@name='agree']").click()
driver.find_element(By.XPATH,"//input[@id='button-payment-method']").click()
time.sleep(1)
driver.save_screenshot("Exigence 07-1 Utilisateur est informé .png")

# Vider la corbeille
driver.find_element(By.XPATH,"//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[@title='Remove']").click()
# Fermer le navigateur
driver.quit()