import pytest
from selenium import webdriver
from selenium_4.pages.cookie import Cookie
from selenium_4.pages.local_storage import LocalStorage


@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome('../drivers/chromedriver')
    browser.get('https://novaposhta.ua/')
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def cookie(browser) -> Cookie:
    yield Cookie(browser)


@pytest.fixture
def local_storage(browser) -> LocalStorage:
    yield LocalStorage(browser)
