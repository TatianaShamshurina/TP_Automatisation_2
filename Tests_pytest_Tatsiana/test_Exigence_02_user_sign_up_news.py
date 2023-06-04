import exigence_02_steps



class TestUserSignUpNews(exigence_02_steps.Steps_02):

    def test_user_sign_up_news(self):
        self.open_page("http://tutorialsninja.com/demo/index.php?route=common/home")
        self.user_register()
        self.remplir_formulaire()
        self.soumettre_formulaire()
        self.close_browser()
