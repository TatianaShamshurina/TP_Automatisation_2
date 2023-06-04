import exigence_01_steps



class TestUserSignUp(exigence_01_steps.Steps_01):

    def test_user_to_register(self):
        self.open_page("http://tutorialsninja.com/demo/index.php?route=common/home")
        self.user_register()
        self.remplir_formulaire()
        self.soumettre_formulaire()
        self.close_browser()
