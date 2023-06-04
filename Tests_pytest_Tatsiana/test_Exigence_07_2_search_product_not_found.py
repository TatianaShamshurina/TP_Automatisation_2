import exigence_07_2_steps

class TestUserSearchProductNotFound(exigence_07_2_steps.Steps_07_2):

    def test_search_product_not_found(self):
        self.open_page("http://tutorialsninja.com/demo/index.php?route=common/home")
        self.user_login()
        self.user_credentials()
        self.user_search_product()
        self.product_not_affiche()
        self.close_browser()