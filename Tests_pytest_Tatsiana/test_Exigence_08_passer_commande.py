# Precondition:
# Compte existe avec:
# first name = 'John'
# last name = 'Travolta'
# email: "jtravolta@rabah.com"

import time
from telnetlib import EC
import exigence_08_steps

class TestUserBuyProduct(exigence_08_steps.Steps_08):

    def test_user_buy_product(self):
        self.open_page("http://tutorialsninja.com/demo/index.php?route=common/home")
        self.user_login()
        self.user_credentials()
        self.user_search_product()
        self.product_affiche()
        self.choose_product()
        self.close_browser()