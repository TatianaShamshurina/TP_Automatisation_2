# Precondition:
# Creer compte avec:
# first name = 'John'
# last name = 'Travolta'
# email: jtravolta@rabah.com

import exigence_03_steps



class TestUserAccountExiste(exigence_03_steps.Steps_03):

    def test_user_account_existe(self):
        self.open_page("http://tutorialsninja.com/demo/index.php?route=common/home")
        self.user_register()
        self.remplir_formulaire()
        self.soumettre_formulaire()
        self.close_browser()
