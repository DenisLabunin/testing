import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def browser(request):
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    request.cls.browser = browser
    yield browser
    browser.quit()
