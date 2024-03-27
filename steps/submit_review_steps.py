import time

from behave import *


@given('I am on the watch model URL')
def step_impl(context):
    context.submit_review_page.open()

@then('The URL ofe the page is "https://magento.softwaretestingboard.com/dash-digital-watch.html"')
def step_impl(context):
    context.submit_review_page.verify_watch_model_url


@when('I click the Reviews button')
def step_impl(context):
    context.submit_review_page.click_reviews_button()
    time.sleep(4)

@when("I set the Nickname")
def step_impl(context):
    context.submit_review_page.set_nickname("TestAnca")

@when('I set the Summary')
def step_impl(context):
    context.submit_review_page.set_summary("Very nice watch!")

@when('I set the Review')
def step_impl(context):
    context.submit_review_page.set_review("It is a very nice watch!")

@when("I set one star rating")
def step_impl(context):
    context.submit_review_page.set_one_star_rating()


@when('I click on Submit Review button')
def step_impl(context):
    context.submit_review_page.click_submit_review_button()

@then('I should see "You submitted your review for moderation." message')
def step_impl(context):
    context.submit_review_page.confirm_submit_message("You submitted your review for moderation.")