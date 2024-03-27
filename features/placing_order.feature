Feature: Placing an order
  @order
  Scenario: Proceed to checkout
    Given I am on the search page
    When I click the watch I want to order
    When I click add to cart the watch
    When I click the show cart button
    When I click view edit cart
    When I am on the edit cart page
    When I click on Proceed to Checkout button
    When I am redirect to shopping address URL
    When I input email address
    When I input first name
    When I input last name
    When I input street address
    When I input city
    When I set country
    When I set state
    When I input zip code
    When I input phone number
    When I click Next button
    When I click Place Order button
    Then I should see the "Thank you for your purchase!" message




