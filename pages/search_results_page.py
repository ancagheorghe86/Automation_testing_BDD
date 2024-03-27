
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

'''Feature: Search

  Background: Open home page
    Given I am on the home page

  Scenario: Search works properly for existing items
    When I enter "Dash" in the search field
    And I click the search button
    Then I am redirected to the search results page'''


class SearchResultsPage(BasePage):
    PRODUCT_TITLE = (By.CLASS_NAME, "product-item-link")
    BUTTON_ADD_TO_CART = (By.XPATH, '//*[@id="product-addtocart-button"]')

    HOME_PAGE_URL = "https://magento.softwaretestingboard.com/"
    SEARCH_RESULTS_PAGE_URL = "https://magento.softwaretestingboard.com/catalogsearch/result/?q=dash"


    def open(self):
        self.driver.get(self.SEARCH_RESULTS_PAGE_URL)

    def verify_url(self):
        assert self.driver.current_url == self.HOME_PAGE_URL

    def verify_url_search(self):
        assert "https://magento.softwaretestingboard.com/catalogsearch/result/?q=" in self.SEARCH_RESULTS_PAGE_URL

    def verify_search_results_displayed(self):
        results = self.find_all(self.PRODUCT_TITLE)
        assert len(results) > 0

    def click_add_to_cart(self):
        self.find(self.BUTTON_ADD_TO_CART).click()
