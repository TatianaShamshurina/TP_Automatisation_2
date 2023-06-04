import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Verifier si les 3 pages s'ouvrent correctement
class TestPages: # Test Class

    def setup(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    @pytest.mark.parametrize(
        "page", [
            "https://tutorialsninja.com/demo/index.php?route=common/home", # URL pour le test 1
            "https://tutorialsninja.com/demo/index.php?route=account/register", # URL pour le test 2
            "https://tutorialsninja.com/demo/index.php?route=account/login" # URL pour le test 3
        ]
    )
    def test_open_pages(self, page):
        self.driver.get(page)
        assert self.driver.current_url == page, "Page was not open"


    def teardown(self):
        self.driver.close()

