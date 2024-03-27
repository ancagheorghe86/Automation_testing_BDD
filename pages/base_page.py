from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser import Browser



class BasePage(Browser):

    driver = webdriver.Chrome()
    driver.maximize_window()


    INPUT_SEARCH = (By.ID, "search")
    BUTTON_SEARCH = (By.XPATH, '//*[@id="search_mini_form"]/div[2]/button')
    CART_QUANTITY = (By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/a/span[2]')
    DIV_EMPTY_MESSAGE = (By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[3]')


    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def select_dropdown_text(self, locator, text):
        dropdown = Select(self.find(locator))
        dropdown.select_by_visible_text(text)

    def set_search_term(self, text):
        self.type(self.INPUT_SEARCH, text)

    def click_search_button(self):
        self.find(self.BUTTON_SEARCH).click()


    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def verify_cart_not_empty(self):
        assert "(0)" not in self.find(self.CART_QUANTITY).text

    def verify_cart_is_empty(self, text):
        assert text in self.find(self.DIV_EMPTY_MESSAGE).text


'''
def select_dropdown_text(self, locator, text):
    dropdown = Select(self.find(locator))  *importam Selectul din selenium
    dropdown.select_by_visible_text(text)
    
    *daca am scris asta in BasePage, practic am parametrizat dropdow-ul
'''