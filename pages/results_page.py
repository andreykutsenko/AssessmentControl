from selenium.webdriver.common.by import By
from pages.base_page import Page


class ResultsPage(Page):
    TOOLBAR_TEXT = (By.XPATH, "//div[@class='info']/h3")
    CONFIRMATION_TITLE = (By.CSS_SELECTOR, '.mat-card h4')
    TEXT_REQUIRED_LOCATOR = (By.ID, 'mat-error-1')

    def verify_username(self, username: str):
        self.verify_element_text(username, *self.TOOLBAR_TEXT)

    def verify_title_page(self, text: str):
        self.verify_element_text(text, *self.CONFIRMATION_TITLE)

    def verify_text_on_page(self, text: str):
        self.verify_element_text(text, *self.TEXT_REQUIRED_LOCATOR)