from browser import Browser
from pages.add_to_cart_page import AddToCartPage
from pages.edit_cart_page import EditCartPage
from pages.home_page import HomePage

from pages.login_page import LoginPage
from pages.placing_order_page import PlacingOrderPage
from pages.register_page import RegisterPage
from pages.search_results_page import SearchResultsPage
from pages.submit_review_page import SubmitReviewPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()
    context.add_to_cart_page = AddToCartPage()
    context.edit_cart_page = EditCartPage()
    context.submit_review_page = SubmitReviewPage()
    context.placing_order_page = PlacingOrderPage()

def after_all(context):
    context.browser.close()
