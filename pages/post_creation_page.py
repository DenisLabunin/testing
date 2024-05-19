from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


class PostCreation(BasePage):

    TITLE_FIELD = (By.CSS_SELECTOR, 'input#title')
    CONTENT_FIELD = (By.CSS_SELECTOR, 'div.ql-editor.ql-blank p')
    AUTHOR_FIELD = (By.CSS_SELECTOR, 'input#author')
    CREATE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    SUCCESS = (By.XPATH, '//p[text()="Post was successfully created!"]')

    TITLE = 'Interesting story'
    CONTENT = 'Very interesting story'
    AUTHOR = 'Noname'
    CURRENT_TIME = None

    AUTHOR_POST = (By.XPATH, '//tbody/tr[last()]/td[2]')
    TITLE_POST = (By.XPATH, '//tbody/tr[last()]/td[3]')
    DATE_POST = (By.XPATH, '//tbody/tr[last()]/td[4]')
    DELETE_BUTTON = (By.XPATH, '//tbody/tr[last()]/td[5]/button[text()=" Delete "]')
    DELETE_SUCCESS = (By.XPATH, '//p[text()="Post was deleted successfully"]')

    def enter_all_field(self):
        self.wait.until(EC.element_to_be_clickable(self.TITLE_FIELD)).send_keys(self.TITLE)
        self.wait.until(EC.element_to_be_clickable(self.CONTENT_FIELD)).send_keys(self.CONTENT)
        self.wait.until(EC.element_to_be_clickable(self.AUTHOR_FIELD)).send_keys(self.AUTHOR)
        self.wait.until(EC.element_to_be_clickable(self.CREATE_BUTTON)).click()
        # for windows use: ('%B %#d, %Y, %#I:%M:%S %p')
        PostCreation.CURRENT_TIME = datetime.now().strftime('%B %-d, %Y, %-I:%M:%S %p')
        assert self.wait.until(EC.visibility_of_element_located(self.SUCCESS)).is_displayed()

    def data_last_post(self):
        title = self.wait.until(EC.visibility_of_element_located(self.TITLE_POST)).text
        author = self.wait.until(EC.visibility_of_element_located(self.AUTHOR_POST)).text
        date = self.wait.until(EC.visibility_of_element_located(self.DATE_POST)).text
        assert (title, author, date) == (self.TITLE, self.AUTHOR, self.CURRENT_TIME), 'Error find post'
        self.wait.until(EC.visibility_of_element_located(self.DELETE_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.DELETE_SUCCESS))
