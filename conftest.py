import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='class')
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(8)
    yield browser
    browser.quit()
