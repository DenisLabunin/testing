from pages.login_page import LoginPage
from pages.post_creation_page import PostCreation
from pages.validation_messages_page import ValidMessages
import pytest


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser
        request.cls.login_page = LoginPage(browser)
        request.cls.post_creation_page = PostCreation(browser)
        request.cls.validation_messages_page = ValidMessages(browser)
