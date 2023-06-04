# Creer compte avec:
# first name = 'John'
# last name = 'Travolta'
# email: jtravolta@rabah.com

import exigence_04_steps

class TestUserLogin(exigence_04_steps.Steps_04):

    def test_user_login(self):
        self.open_page("http://tutorialsninja.com/demo/index.php?route=common/home")
        self.user_login()
        self.user_credentials()
        self.user_account()
        self.close_browser()
