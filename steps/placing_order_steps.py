import time

from behave import *


@given("I am on the search page")
def step_impl(context):
    context.add_to_cart_page.open()

@when('I click the watch I want to order')
def step_impl(context):
    context.add_to_cart_page.select_watch()


@when('I click add to cart the watch')
def step_impl(context):
    context.search_results_page.click_add_to_cart()
    time.sleep(5)

@when('I click the show cart button')
def step_impl(context):
    context.placing_order_page.show_cart()


@when('I click view edit cart')
def step_impl(context):
    context.placing_order_page.view_edit_cart()

@when('I am on the edit cart page')
def step_impl(context):
    context.edit_cart_page.open()


@when('I click on Proceed to Checkout button')
def step_impl(context):
    context.placing_order_page.click_proceed_to_checkout_button()
    time.sleep(5)


@when('I am redirect to shopping address URL')
def step_impl(context):
    context.placing_order_page.verify_shipping_url()


@when('I input email address')
def step_impl(context):
    context.placing_order_page.set_email("testtest123@gmail.com")


@when('I input first name')
def step_impl(context):
    context.placing_order_page.set_first_name("testtest123")

@when('I input last name')
def step_impl(context):
    context.placing_order_page.set_last_name("testtest1234")

@when('I input street address')
def step_impl(context):
    context.placing_order_page.set_street_address("Calea Victoriei")

@when('I input city')
def step_impl(context):
    context.placing_order_page.set_city("Bucharest")

@when('I set country')
def step_impl(context):
    context.placing_order_page.set_country('Romania')
    time.sleep(3)

@when('I set state')
def step_impl(context):
    context.placing_order_page.set_state("Bucureşti")

@when('I input zip code')
def step_impl(context):
    context.placing_order_page.set_zip_code('030026')

@when('I input phone number')
def step_impl(context):
    context.placing_order_page.set_phone_number("1234567890")

@when('I click Next button')
def step_impl(context):
    context.placing_order_page.click_button_next()
    time.sleep(5)

@when('I click Place Order button')
def step_impl(context):
    context.placing_order_page.click_button_place_order()
    time.sleep(10)

@then('I should see the "Thank you for your purchase!" message')
def step_impl(context):
    context.placing_order_page.verify_order_confirm_message("Thank you for your purchase!")
