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

class Steps_04:


    def setup(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()



    def open_page(self,url):
        self.driver.get(url)

    def user_login(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        self.register_link = self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']")
        self.register_link.click()

    def user_credentials(self):
        self.email = 'jtravolta@rabah.com'
        self.password = "password"
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(self.email)
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys(self.password)
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def user_account(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Edit your account information']").is_displayed()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Edit your account information']").click()
        self.driver.implicitly_wait(10)
        self.user_email = self.driver.find_element(By.XPATH,"//input[@id='input-email'][@value='jtravolta@rabah.com']").is_displayed()

        self.driver.save_screenshot("Exigence 04 user_login.png")

    def close_browser(self):
        self.driver.close()
