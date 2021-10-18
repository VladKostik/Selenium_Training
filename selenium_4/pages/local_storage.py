from selenium.webdriver.chrome.webdriver import WebDriver


class LocalStorage:
    def __init__(self, browser: WebDriver):
        self._browser = browser

    def _add_one(self, name: str, data: str):
        self._browser.execute_script(
            f"window.localStorage['{name}'] = '{data}'"
        )

    def _get_one_by_name(self, name: str):
        return self._browser.execute_script(
            f"return window.localStorage['{name}']"
        )

    def _get_all(self):
        return self._browser.execute_script(
            f"return window.localStorage;"
        )
