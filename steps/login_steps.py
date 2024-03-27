import time

from behave import *

@given("I am on the login page")
def step_impl(context):
    context.login_page.open()

@then('The URL of the page is "https://magento.softwaretestingboard.com/customer/account/login"')
def step_impl(context):
    context.login_page.verify_url()

@when('I enter "{text}" as email')
def step_impl(context, text):
    context.login_page.set_email(text)

@when('I enter "{text}" as password')
def step_impl(context, text):
    context.login_page.set_password(text)

@when('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()

    time.sleep(3)

@then('I should see "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." message')
def step_impl(context):
    context.login_page.verify_login_error_message("The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.")
