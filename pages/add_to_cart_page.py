
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddToCartPage(BasePage):

    SEARCH_RESULTS_PAGE_URL = "https://magento.softwaretestingboard.com/catalogsearch/result/?q=dash"
    WATCH_MODEL = (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/div[2]/ol/li[1]/div/div/strong/a')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#maincontent > div.page.messages > div:nth-child(2) > div > div > div')

    def open(self):
        self.driver.get(self.SEARCH_RESULTS_PAGE_URL)

    def verify_url(self):
        assert self.driver.current_url == self.SEARCH_RESULTS_PAGE_URL

    def verify_success_message(self):
        assert "You added Dash Digital Watch to your shopping cart." in self.find(self.SUCCESS_MESSAGE)

    def select_watch(self):
        self.find(self.WATCH_MODEL).click()

