from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app.logger import logger
from time import sleep


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    def open_page(self, url: str):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input(self, text: str, *locator):
        input_field = self.find_element(*locator)
        input_field.clear()
        logger.info(f'Input text: {text}')
        input_field.send_keys(text)

    def click(self, *locator):
        self.find_element(*locator).click()

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_visible(self, *locator):
        self.driver.wait.until(EC.visibility_of_element_located(locator))

    def verify_element_text(self, expected_text: str, *locator):
        self.wait_for_element_visible(*locator)
        sleep(3)
        actual_text = self.find_element(*locator).text
        logger.info(f'Actual text: {actual_text}')
        assert expected_text in actual_text, f'Expected {expected_text} text, but got {actual_text} text'