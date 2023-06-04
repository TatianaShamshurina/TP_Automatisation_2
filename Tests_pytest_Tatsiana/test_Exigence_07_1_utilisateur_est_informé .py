import exigence_07_1_steps

class TestUserWantBuyProduct(exigence_07_1_steps.Steps_07_1):

    def test_user_want_to_by_product(self):
        self.open_page("http://tutorialsninja.com/demo/index.php?route=common/home")
        self.user_login()
        self.user_credentials()
        self.user_search_product()
        self.product_affiche()
        self.choose_product()
        self.vider_corbeille()
        self.close_browser()