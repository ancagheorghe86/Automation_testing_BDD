import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage



class RegisterPage(BasePage):

    REGISTER_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/create/"
    INPUT_FIRST_NAME = (By.ID, "firstname")
    INPUT_LAST_NAME = (By.ID,"lastname")
    INPUT_EMAIL = (By.ID, "email_address")
    INPUT_PASSWORD = (By.ID, "password")
    INPUT_CONFIRM_PASSWORD = (By.ID, "password-confirmation")
    BUTTON_REGISTER = (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button/span')
    LOGGED_IN_MESSAGE = (By.CLASS_NAME, "logged-in")

    def open(self):
        self.driver.get(self.REGISTER_PAGE_URL)

    time.sleep(3)

    def verify_url(self):
         assert self.driver.current_url == self.REGISTER_PAGE_URL

    def set_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)

    def set_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def set_confirm_password(self, text):
        self.type(self.INPUT_CONFIRM_PASSWORD, text)

    def click_register_button(self):
        self.find(self.BUTTON_REGISTER).click()

    def confirm_logged_in(self):
        self.find(self.LOGGED_IN_MESSAGE).text


'''
def select_bith_day(self, text):
    dropdown = Select(self.find(self.Select_BIRTH_DAY))
    dropdown.select_by_visible_text(text)
'''
