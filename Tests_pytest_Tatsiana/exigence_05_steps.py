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

class Steps_05:


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

    def user_forgot_password(self):
        self.email = 'jtravolta@rabah.com'
        self.driver.find_element(By.XPATH, "//div[@class='form-group']//a[normalize-space()='Forgotten Password']").click()

        # Wait until the element is displayed
        self.wait = WebDriverWait(self.driver, 10)  # Maximum wait time of 10 seconds
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(self.email)
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()

        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//*[contains(text(),'An email with a confirmation link has been sent your email address.')]").is_displayed()

        self.driver.save_screenshot("Exigence 05 User forgot password.png")

    def close_browser(self):
        self.driver.close()

