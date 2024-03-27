import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class PlacingOrderPage(BasePage):

    SHOW_CART_BUTTON = (By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/a')
    VIEW_EDIT_CART = (By.XPATH, '//*[@id="minicart-content-wrapper"]/div[2]/div[5]/div/a/span')
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[3]/div[1]/ul/li[1]/button')
    SHIPPING_ADDRESS_URL = "https://magento.softwaretestingboard.com/checkout/#shipping"
    INPUT_EMAIL_ADDRESS = (By.XPATH, '//*[@id="customer-email"]')
    INPUT_FIRST_NAME = (By.NAME, 'firstname')
    INPUT_LAST_NAME = (By.NAME, 'lastname')
    INPUT_STREET_ADDRESS = (By.NAME, 'street[0]')
    INPUT_CITY = (By.NAME, 'city')
    SELECT_STATE = (By.NAME, 'region_id')
    INPUT_ZIP_CODE = (By.NAME, 'postcode')
    SELECT_COUNTRY = (By.NAME, 'country_id')
    INPUT_PHONE_NUMBER = (By.NAME, 'telephone')
    BUTTON_NEXT = (By.XPATH, '//*[@id="shipping-method-buttons-container"]/div/button')
    BUTTON_PLACE_ORDER = (By.XPATH, '//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button')
    ORDER_CONFIRM_MESSAGE = (By.XPATH, '//*[@id="maincontent"]/div[1]/h1/span')



    def open(self):
        self.driver.get(self.SHIPPING_ADDRESS_URL)

    def verify_shipping_url(self):
        assert self.driver.current_url == self.SHIPPING_ADDRESS_URL

    def show_cart(self):
        self.find(self.SHOW_CART_BUTTON).click()

    def view_edit_cart(self):
        self.find(self.VIEW_EDIT_CART).click()
        time.sleep(5)

    def click_proceed_to_checkout_button(self):
        self.find(self.PROCEED_TO_CHECKOUT_BUTTON).click()

    def set_email(self, text):
        self.type(self.INPUT_EMAIL_ADDRESS, text)

    def set_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)

    def set_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)

    def set_street_address(self, text):
        self.type(self.INPUT_STREET_ADDRESS, text)

    def set_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)

    def set_street_address(self, text):
        self.type(self.INPUT_STREET_ADDRESS, text)

    def set_city(self, text):
        self.type(self.INPUT_CITY, text)

    def set_state(self, text):
        dropdown = Select(self.find((self.SELECT_STATE)))
        dropdown.select_by_visible_text(text)

    def set_zip_code(self, text):
        self.type(self.INPUT_ZIP_CODE, text)

    def set_country(self, text):
        dropdown = Select(self.find((self.SELECT_COUNTRY)))
        dropdown.select_by_visible_text(text)

    def set_phone_number(self, text):
        self.type(self.INPUT_PHONE_NUMBER, text)

    def click_button_next(self):
        self.find(self.BUTTON_NEXT).click()

    def click_button_place_order(self):
        self.find(self.BUTTON_PLACE_ORDER).click()

    def verify_order_confirm_message(self, text):
        assert text in self.find(self.ORDER_CONFIRM_MESSAGE).text


