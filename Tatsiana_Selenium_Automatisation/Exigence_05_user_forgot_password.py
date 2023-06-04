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

# Cliquer sur le lien d'inscription
register_link = driver.find_element(By.XPATH,"//a[normalize-space()='Login']")
register_link.click()

email = 'jtravolta@rabah.com'
driver.find_element(By.XPATH,"//div[@class='form-group']//a[normalize-space()='Forgotten Password']").click()

#Wait until the element is displayed
wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds

driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys(email)
driver.find_element(By.XPATH,"//input[@value='Continue']").click()

driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//*[contains(text(),'An email with a confirmation link has been sent your email address.')]").is_displayed()

driver.save_screenshot("Exigence 05 User forgot password.png")

# Fermer le navigateur
driver.quit()