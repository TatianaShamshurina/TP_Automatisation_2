import exigence_05_steps

class TestUserForgotPassword(exigence_05_steps.Steps_05):

    def test_user_forgotten_password(self):
        self.open_page("http://tutorialsninja.com/demo/index.php?route=common/home")
        self.user_login()
        self.user_forgot_password()
        self.close_browser()