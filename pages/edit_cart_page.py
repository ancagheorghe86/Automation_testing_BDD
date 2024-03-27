
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class EditCartPage(BasePage):

    BUTTON_REMOVE_ITEM = (By.XPATH, '//*[@id="shopping-cart-table"]/tbody/tr[2]/td/div/a[2]')
    SHOPPING_CART_URL = "https://magento.softwaretestingboard.com/checkout/cart/"


    def open(self):
        self.driver.get(self.SHOPPING_CART_URL)

    def verify_cart_url(self):
        assert self.driver.current_url == self.SHOPPING_CART_URL

    def click_remove_item_button(self):
        self.find(self.BUTTON_REMOVE_ITEM).click()



