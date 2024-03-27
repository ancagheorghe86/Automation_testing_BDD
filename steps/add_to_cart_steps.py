import time

from behave import *

@given("I am on the search results page")
def step_impl(context):
    context.add_to_cart_page.open()

@then('The URL of the page is "https://magento.softwaretestingboard.com/catalogsearch/result/?q=dash"')
def step_impl(context):
    context.add_to_cart_page.verify_url()

@when('I click the watch I want')
def step_impl(context):
    context.add_to_cart_page.select_watch()


@when('I click add to cart')
def step_impl(context):
    context.search_results_page.click_add_to_cart()
    time.sleep(5)


@then('Cart not empty')
def step_impl(context):
    context.add_to_cart_page.verify_cart_not_empty()


