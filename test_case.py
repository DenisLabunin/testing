from selenium.webdriver.common.by import By
import os
import time
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()
SITE = os.getenv('URL_SITE')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


class TestWebSite:
    title_name = 'title'
    author_name = 'author'
    current_date = ''

    def test_successful_log_in(self, browser):
        browser.get(SITE + '/admin/login')
        email = browser.find_element(By.CSS_SELECTOR, 'input#email')
        email.send_keys(LOGIN)
        passw = browser.find_element(By.CSS_SELECTOR, 'input#password')
        passw.send_keys(PASSWORD)
        button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button.click()
        time.sleep(3)
        assert browser.current_url == f'{SITE}/admin/dashboard', "Login failed"

    def test_successful_post_creation(self, browser):
        browser.get(SITE + '/admin/create')
        title = browser.find_element(By.CSS_SELECTOR, 'input#title')
        title.send_keys(TestWebSite.title_name)
        content = browser.find_element(By.CSS_SELECTOR, 'div.ql-editor.ql-blank p')
        content.send_keys('post content')
        author = browser.find_element(By.CSS_SELECTOR, 'input#author')
        author.send_keys(TestWebSite.author_name)
        button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        TestWebSite.current_date = str(datetime.now().strftime('%B %#d, %Y, %#I:%M:%S %p'))
        button.click()
        success = browser.find_element(By.XPATH, '//p[text()="Post was successfully created!"]').text
        assert success == 'Post was successfully created!', "Post was not created"

        browser.get(SITE + '/admin/dashboard')
        author_1 = browser.find_element(By.XPATH, '//tbody/tr[last()]/td[2]').text
        title_1 = browser.find_element(By.XPATH, '//tbody/tr[last()]/td[3]').text
        date_1 = browser.find_element(By.XPATH, '//tbody/tr[last()]/td[4]').text
        assert (author_1, title_1, date_1) == \
               (TestWebSite.author_name, TestWebSite.title_name, TestWebSite.current_date), \
               "The post did not appear on the dashboard"
        delete = browser.find_element(By.XPATH, '//tbody/tr[last()]/td[5]/button[text()=" Delete "]')
        delete.click()
        browser.find_element(By.XPATH, '//p[text()="Post was deleted successfully"]')

    def test_validation_messages(self, browser):
        browser.get(SITE + '/admin/create')
        button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button.click()
        title_invalid = browser.find_element(By.XPATH, '//div[contains(@class, "form-control")][1]'
                                                       '/div[contains(@class, "validation")]').is_displayed()
        post_invalid = browser.find_element(By.XPATH, '//div[contains(@class, "form-control")][2]'
                                                      '/div[contains(@class, "validation")]').is_displayed()
        author_invalid = browser.find_element(By.XPATH, '//div[contains(@class, "form-control")][3]'
                                                        '/div[contains(@class, "validation")]').is_displayed()
        assert all((title_invalid, post_invalid, author_invalid))
