
import time

from pages.base_page import BasePage

from selenium.webdriver.common.by import By
class SubmitReviewPage(BasePage):

    WATCH_MODEL_URL = "https://magento.softwaretestingboard.com/dash-digital-watch.html"
    REVIEWS_BUTTON = (By.XPATH, '//*[@id="tab-label-reviews-title"]')
    INPUT_NICKNAME = (By.ID, "nickname_field")
    INPUT_SUMMARY = (By.ID, "summary_field")
    INPUT_REVIEW = (By.ID, "review_field")
    BUTTON_SUBMIT_REVIEW = (By.XPATH, '//*[@id="review-form"]/div/div/button')
    ONE_STARS_RATING = (By.ID, 'Rating_1_label')
    DIV_SUBMIT_MESSAGE = (By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div')
    def open(self):
        self.driver.get(self.WATCH_MODEL_URL)

    def verify_watch_model_url(self):
        assert self.driver.current_url == self.WATCH_MODEL_URL

    def click_reviews_button(self):
        self.find(self.REVIEWS_BUTTON).click()

    def set_nickname(self, text):
        self.type(self.INPUT_NICKNAME, text)

    def set_summary(self, text):
        self.type(self.INPUT_SUMMARY, text)

    def set_review(self, text):
        self.type(self.INPUT_REVIEW, text)

    def set_one_star_rating(self):
        self.find(self.ONE_STARS_RATING).click()


    def click_submit_review_button(self):
        self.find(self.BUTTON_SUBMIT_REVIEW).click()
        time.sleep(5)

    def confirm_submit_message(self, text):
        assert text in self.find(self.DIV_SUBMIT_MESSAGE).text


