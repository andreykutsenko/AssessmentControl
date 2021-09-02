from selenium.webdriver.common.by import By
from pages.base_page import Page


class LoginPage(Page):
    LOGINID_FIELD = (By.ID, 'mat-input-0')
    PASSWORD_FIELD = (By.ID, 'mat-input-1')
    SIGNIN_BUTTON = (By.CSS_SELECTOR, '.mat-raised-button.mat-primary')
    REGISTER_LINK = (By.CSS_SELECTOR, 'a .mat-button-wrapper')
    REGISTERME_BUTTON = (By.CSS_SELECTOR, '.mat-raised-button.mat-primary')
    FIRSTNAME_FIELD = (By.XPATH, "//input[@formcontrolname='firstName']")
    LASTNAME_FIELD = (By.XPATH, "//input[@formcontrolname='lastName']")
    EMAIL_FIELD = (By.XPATH, "//input[@formcontrolname='email']")
    GROUPCODE_FIELD = (By.XPATH, "//input[@formcontrolname='group']")
    REG_PASSWORD_FIELD = (By.XPATH, "//input[@formcontrolname='password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@formcontrolname='confirmPassword']")
    FOGOT_PASSWORD_LINK = (By.CSS_SELECTOR, '.ng-untouched.ng-pristine.ng-invalid a')
    RESET_PASSWORD_BTN = (By.CSS_SELECTOR, '.controls .mat-button-wrapper')

    def open_login(self):
        self.open_page('http://ask-qa.portnov.com/#/login')

    def filling_login_fields(self, email: str, password: str):
        self.input(email, *self.LOGINID_FIELD)
        self.input(password, *self.PASSWORD_FIELD)

    def filling_email_field(self, email: str):
        self.input(email, *self.EMAIL_FIELD)

    def click_signin_button(self):
        self.click(*self.SIGNIN_BUTTON)

    def click_register_now(self):
        self.click(*self.REGISTER_LINK)

    def click_register_me(self):
        self.click(*self.REGISTERME_BUTTON)

    def click_fogot_password(self):
        self.click(*self.FOGOT_PASSWORD_LINK)

    def click_password_reset(self):
        self.click(*self.RESET_PASSWORD_BTN)

    def filling_fields(self, context):
        for row in context.table:
            self.input(row['FirstName'], *self.FIRSTNAME_FIELD)
            self.input(row['LastName'], *self.LASTNAME_FIELD)
            self.input(row['Email'], *self.EMAIL_FIELD)
            self.input(row['GroupCode'], *self.GROUPCODE_FIELD)
            self.input(row['Password'], *self.REG_PASSWORD_FIELD)
            self.input(row['Password'], *self.CONFIRM_PASSWORD_FIELD)