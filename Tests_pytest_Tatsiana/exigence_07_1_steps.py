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

class Steps_07_1:


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

    def user_search_product(self):
        self.product = 'Samsung'
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").is_displayed()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys(self.product)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()

    def product_affiche(self):
        # Wait until the element is displayed
        self.wait = WebDriverWait(self.driver, 10)  # Maximum wait time of 10 seconds
        self.driver.find_element(By.XPATH, "//h1[contains(text(),'Samsung')]").is_displayed()

    def choose_product(self):
        # Wait until the element is displayed
        self.wait = WebDriverWait(self.driver, 10)  # Maximum wait time of 10 seconds
        self.driver.find_element(By.XPATH, "//h1[contains(text(),'Samsung')]").is_displayed()
        self.driver.find_element(By.XPATH, "//div[@class='caption']//a[contains(text(),'Samsung SyncMaster 941BW')]").click()
        self.driver.find_element(By.XPATH, "//button[@id='button-cart']").click()
        self.driver.find_element(By.XPATH, "//span[@id='cart-total'][contains(text(),' 1 item(s) - $200.00')]").is_displayed()
        self.driver.find_element(By.XPATH, "//span[@id='cart-total'][contains(text(),' 1 item(s) - $200.00')]").click()
        self.driver.find_element(By.XPATH, "//p[@class='text-right']/a[2]//i").click()
        self.driver.find_element(By.XPATH, "//input[@id='button-payment-address']").click()
        self.driver.find_element(By.XPATH, "//input[@id='button-shipping-address']").click()
        self.driver.find_element(By.XPATH, "//input[@id='button-shipping-method']").click()
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        self.driver.find_element(By.XPATH, "//input[@id='button-payment-method']").click()
        time.sleep(1)

        self.driver.save_screenshot("Exigence 07_1 Utilisateur est informé .png")

    #Postconditions:
    def vider_corbeille(self):
        # Vider la corbeille
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@title='Remove']").click()

    def close_browser(self):
        self.driver.close()