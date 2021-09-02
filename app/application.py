from pages.login_page import LoginPage
from pages.results_page import ResultsPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.login_page = LoginPage(self.driver)
        self.results_page = ResultsPage(self.driver)