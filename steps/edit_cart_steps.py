import time

from behave import *
'''
Feature: Edit cart
  @editcart
  Scenario: Check that the shopping cart page URL is correct
    Given I am on the shopping cart page
    Then The URL of the page is "https://magento.softwaretestingboard.com/checkout/cart/"
  @editcart
  Scenario: Remove item from the cart
    Given I am on the shopping cart page
    When I click the Remove item button
    Then Cart is empty
'''
@given('I am on the shopping cart page')
def step_impl(context):
    context.edit_cart_page.open()

@then('The URL of the page is "https://magento.softwaretestingboard.com/checkout/cart/"')
def step_impl(context):
    context.edit_cart_page.verify_cart_url()

@when('I click the Remove item button')
def step_impl(context):
    context.edit_cart_page.click_remove_item_button()
    time.sleep(5)

@then('I should see "You have no items in your shopping cart." message')
def step_impl(context):
    context.edit_cart_page.verify_cart_is_empty("You have no items in your shopping cart.")

