import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import datetime



class Steps_03:
    def setup(self):

        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()

    def open_page(self,url):
        self.driver.get(url)

    def user_register(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        register_link = self.driver.find_element(By.LINK_TEXT, 'Register')
        register_link.click()

    def remplir_formulaire(self):
        self.first_name = self.driver.find_element(By.ID, 'input-firstname')
        self.first_name.send_keys('John')

        self.last_name = self.driver.find_element(By.ID, 'input-lastname')
        self.last_name.send_keys('Travolta')

        self.email = self.driver.find_element(By.ID, 'input-email')
        self.email.send_keys('jtravolta@rabah.com')

        self.telephone = self.driver.find_element(By.ID, 'input-telephone')
        self.telephone.send_keys('1234567890')

        self.password = self.driver.find_element(By.ID, 'input-password')
        self.password.send_keys('password')

        self.confirm_password = self.driver.find_element(By.ID, 'input-confirm')
        self.confirm_password.send_keys('password')

        self.privacy_policy = self.driver.find_element(By.NAME, 'agree')
        self.privacy_policy.click()

    def soumettre_formulaire(self):
        self.submit_button = self.driver.find_element(By.XPATH, '//input[@type="submit" and @value="Continue"]')
        self.submit_button.click()

        self.driver.save_screenshot("Exigence 03 account_existe.png")

    def close_browser(self):
        self.driver.close()