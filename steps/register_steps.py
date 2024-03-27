import time

from behave import *

@given("I am on the register page")
def step_impl(context):
    context.register_page.open()

@then('The URL of the page is "https://magento.softwaretestingboard.com/customer/account/create/"')
def step_impl(context):
    context.register_page.verify_url()

@when('I enter first name')
def step_impl(context):
    context.register_page.set_first_name("testtest1")

@when('I enter last name')
def step_impl(context):
    context.register_page.set_last_name("testtest2")

@when('I enter email')
def step_impl(context):
    context.register_page.set_email("testtes123456@gmail.com")

@when('I enter password')
def step_impl(context):
    context.register_page.set_password("TestTest123456*")

@when('I confirm password')
def step_impl(context):
    context.register_page.set_confirm_password("TestTest123456*")

@when('I click the register button')
def step_impl(context):
    context.register_page.click_register_button()

@then('I should be logged in')
def step_impl(context):
    context.register_page.confirm_logged_in()

