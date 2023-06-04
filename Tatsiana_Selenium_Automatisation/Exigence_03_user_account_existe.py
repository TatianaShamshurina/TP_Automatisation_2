# Precondition:
# Creer compte avec:
# first name = 'John'
# last name = 'Travolta'
# email: jtravolta@rabah.com

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

# Cliquer sur le lien d'inscription
register_link = driver.find_element(By.LINK_TEXT, 'Register')
register_link.click()

# Remplir le formulaire d'inscription
first_name = driver.find_element(By.ID, 'input-firstname')
first_name.send_keys('John')

last_name = driver.find_element(By.ID, 'input-lastname')
last_name.send_keys('Travolta')

email = driver.find_element(By.ID, 'input-email')
email.send_keys('jtravolta@rabah.com')

telephone = driver.find_element(By.ID, 'input-telephone')
telephone.send_keys('1234567890')

password = driver.find_element(By.ID, 'input-password')
password.send_keys('password')

confirm_password = driver.find_element(By.ID, 'input-confirm')
confirm_password.send_keys('password')

privacy_policy = driver.find_element(By.NAME, 'agree')
privacy_policy.click()

# Soumettre le formulaire
submit_button = driver.find_element(By.XPATH, '//input[@type="submit" and @value="Continue"]')
submit_button.click()
time.sleep(2)

driver.save_screenshot("Exigence 03 account already existe.png")

# Fermer le navigateur
driver.quit()