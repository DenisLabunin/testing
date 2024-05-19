from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def open(self, url):
        self.browser.get(url)

    def is_opened(self, url):
        self.wait.until(EC.url_to_be(url))