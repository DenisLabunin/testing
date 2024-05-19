from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ValidMessages(BasePage):

    CREATE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    TITLE_INVALID = (By.XPATH, '//div[contains(@class, "form-control")][1]/div[contains(@class, "validation")]')
    POST_INVALID = (By.XPATH, '//div[contains(@class, "form-control")][2]/div[contains(@class, "validation")]')
    AUTHOR_INVALID = (By.XPATH, '//div[contains(@class, "form-control")][3]/div[contains(@class, "validation")]')

    def check_message(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON)).click()
        title_invalid = self.wait.until(EC.visibility_of_element_located(self.TITLE_INVALID)).is_displayed()
        post_invalid = self.wait.until(EC.visibility_of_element_located(self.TITLE_INVALID)).is_displayed()
        author_invalid = self.wait.until(EC.visibility_of_element_located(self.TITLE_INVALID)).is_displayed()
        assert all((title_invalid, post_invalid, author_invalid))
