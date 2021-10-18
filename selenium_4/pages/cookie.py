from selenium.webdriver.chrome.webdriver import WebDriver


class Cookie:
    def __init__(self, browser: WebDriver):
        self._browser = browser

    def _add_one(self, name: str, value: str):
        self._browser.add_cookie({"name": f"{name}", "value": f"{value}"})

    def _get_one(self, name: str):
        return self._browser.get_cookie(f"{name}")

    def _get_all(self):
        return self._browser.get_cookies()
