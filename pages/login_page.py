
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://magento.softwaretestingboard.com/customer/account/login"
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PASSWORD = (By.ID,"pass")
    BUTTON_LOGIN = (By.XPATH, '//*[@id="send2"]/span')
    DIV_ERROR_MESSAGE = (By.XPATH, '//*[@id="maincontent"]/div[2]/div[2]/div/div/div')

    def open(self):
         self.driver.get(self.LOGIN_PAGE_URL)

    def verify_url(self):
         assert self.driver.current_url == self.LOGIN_PAGE_URL


    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_login_button(self):
        self.find(self.BUTTON_LOGIN).click()

    # def verify_no_customer_account_found_message(self):
    #     assert "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." in self.find(self.DIV_ERROR_MESSAGE)

    def verify_login_error_message(self, text):
        assert text in self.find(self.DIV_ERROR_MESSAGE).text



