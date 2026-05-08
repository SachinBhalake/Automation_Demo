from UI_Selenium.waits import Waits
from selenium.webdriver.support.ui import Select


class UIClient:

    def __init__(self, driver, logger):
        self.driver = driver
        self.wait = Waits(driver)
        self.logger = logger

    def highlight(self, element):
        self.scroll_into_view(element)
        self.driver.execute_script(
            "arguments[0].style.border='3px solid red';"
            "arguments[0].style.background='yellow';"
            "setTimeout(()=>{arguments[0].style.border='';"
            "arguments[0].style.background='';},200);",
            element
        )

    def wait_for_page_load(self):
        self.logger.info("Waiting for page load")
        self.wait.wait_for_page_load()

    def get_element(self, locator):
        self.logger.info(f"Finding element: {locator}")
        element = self.wait.visible(locator)
        if not element:
            self.logger.error(f"Element not found: {locator}")
            raise Exception(f"Element not found: {locator}")
        self.highlight(element)
        return element

    def get_elements(self, locator):
        self.logger.info(f"Finding element list: {locator}")
        elements = self.wait.all_visible(locator)
        if not elements:
            self.logger.error(f"Elements not found: {locator}")
            raise Exception(f"Elements not found: {locator}")
        for el in elements:
            self.highlight(el)
        return elements

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        element = self.wait.clickable(locator)
        if not element:
            self.logger.error(f"Element not clickable: {locator}")
            raise Exception(f"Element not clickable: {locator}")
        self.highlight(element)
        try:
            element.click()
            self.logger.info("Click successful")
        except Exception as e1:
            self.logger.warning(f"Normal click failed, trying JS click | {str(e1)[:80]}")
            try:
                self.driver.execute_script("arguments[0].click();", element)
                self.logger.info("JS click successful")
            except Exception as e2:
                self.logger.error(
                    f"Both normal click and JS click failed | "
                    f"JS Error: {str(e2)[:80]}"
                )
                raise

    def send_keys(self, locator, data):
        self.logger.info(f"Typing data into element: {locator}")
        element = self.get_element(locator)
        element.clear()
        element.send_keys(data)

    def get_text(self, locator):
        self.logger.info(f"Getting text from element: {locator}")
        element = self.get_element(locator)
        text = element.text or element.get_attribute("innerText")
        text = text.strip() if text else ""
        self.logger.info(f"Captured text: {text}")
        return text

    def get_title(self):
        self.logger.info(f"Getting page title")
        title = self.driver.title
        self.logger.info(f"Page title: {title}")
        return title

    def get_url(self):
        self.logger.info(f"Getting page url")
        url = self.driver.current_url
        self.logger.info(f"Page url: {url}")
        return url

    def scroll_into_view(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center', inline:'nearest', behavior:'instant'});",
            element
        )

    def get_attribute(self, locator, attr):
        self.logger.info(f"Getting attribute: {attr} of element: {locator}")
        element = self.get_element(locator)
        value = element.get_attribute(attr)
        self.logger.info(f"Attribute value: {value}")
        return value

    def select_dropdown(self, locator, value):
        self.logger.info(f"Selecting dropdown value: {value} of element: {locator}")
        dropdown = Select(self.get_element(locator))
        dropdown.select_by_value(value)

    def accept_alert(self):
        self.logger.info(f"Accepting alert")
        alert = self.wait.alert()
        alert.accept()

    def switch_to_iframe(self, locator):
        self.logger.info(f"Switching to iframe: {locator}")
        iframe = self.wait.presence(locator)
        self.driver.switch_to.frame(iframe)

    def switch_to_default(self):
        self.logger.info("Switching to default content")
        self.driver.switch_to.default_content()