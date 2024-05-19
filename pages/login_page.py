from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    LOGIN_FIELD = (By.CSS_SELECTOR, 'input#email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input#password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_FIELD)).send_keys(login)

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
