import exigence_06_steps

class TestUserSearchProduct(exigence_06_steps.Steps_06):

    def test_user_search_product(self):
        self.open_page("http://tutorialsninja.com/demo/index.php?route=common/home")
        self.user_login()
        self.user_credentials()
        self.user_search_product()
        self.product_affiche()
        self.close_browser()