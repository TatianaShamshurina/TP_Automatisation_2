import pytest
import time
import requests

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def browser(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    request.cls.driver = driver


