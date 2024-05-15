import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(8)
    yield browser
    browser.quit()
