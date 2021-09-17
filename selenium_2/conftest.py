import pytest
from selenium import webdriver
from selenium_2.pages.dashboard import Dashboard


@pytest.fixture(scope='session')
def browser():
    browser = webdriver.Chrome('../drivers/chromedriver')
    browser.get('https://novaposhta.ua/')
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def dashboard(browser) -> Dashboard:
    yield Dashboard(browser)
