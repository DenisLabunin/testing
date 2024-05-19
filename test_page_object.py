from config.data import Data
from base_test import BaseTest
from config.links import Links


class TestWebSite(BaseTest):

    def test_login(self, browser):
        self.login_page.open(Links.LOGIN_PADE)
        self.login_page.enter_login(Data.LOGIN)
        self.login_page.enter_password(Data.PASSWORD)
        self.login_page.click_submit_button()
        self.login_page.is_opened(Links.DASHBOARD_PAGE)

    def test_post_creation(self):
        self.login_page.open(Links.LOGIN_PADE)
        self.login_page.enter_login(Data.LOGIN)
        self.login_page.enter_password(Data.PASSWORD)
        self.login_page.click_submit_button()
        self.login_page.is_opened(Links.DASHBOARD_PAGE)
        self.post_creation_page.open(Links.CREATE_POST_PAGE)
        self.post_creation_page.enter_all_field()
        self.post_creation_page.open(Links.DASHBOARD_PAGE)
        self.post_creation_page.data_last_post()

    def test_validation_messages(self):
        self.login_page.open(Links.LOGIN_PADE)
        self.login_page.enter_login(Data.LOGIN)
        self.login_page.enter_password(Data.PASSWORD)
        self.login_page.click_submit_button()
        self.login_page.is_opened(Links.DASHBOARD_PAGE)
        self.post_creation_page.open(Links.CREATE_POST_PAGE)
        self.validation_messages.check_message()





