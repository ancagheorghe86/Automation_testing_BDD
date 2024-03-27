
from pages.base_page import BasePage


class HomePage(BasePage):

    HOME_PAGE_URL = "https://magento.softwaretestingboard.com"

    def open(self):
         self.driver.get(self.HOME_PAGE_URL)

    def verify_url_search(self):
        assert self.driver.current_url == self.HOME_PAGE_URL


