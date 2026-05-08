from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Waits:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def _wait(self, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout)

    def wait_for_page_load(self):
        try:
            self._wait().until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            return True
        except Exception:
            return False

    def visible(self, locator, timeout=None):
        try:
            return self._wait(timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception:
            return False

    def clickable(self, locator, timeout=None):
        try:
            return self._wait(timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except Exception:
            return False

    def all_visible(self, locator, timeout=None):
        try:
            elements = self._wait(timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return elements if elements else False
        except Exception:
            return False

    def presence(self, locator, timeout=None):
        try:
            return self._wait(timeout).until(
                EC.presence_of_element_located(locator)
            )
        except Exception:
            return False

    def invisible(self, locator, timeout=None):
        try:
            return self._wait(timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except Exception:
            return False

    def alert(self, timeout=None):
        try:
            return self._wait(timeout).until(
                EC.alert_is_present()
            )
        except Exception:
            return False

    def url_contains(self, text, timeout=None):
        try:
            return self._wait(timeout).until(
                EC.url_contains(text)
            )
        except Exception:
            return False