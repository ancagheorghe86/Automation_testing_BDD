Feature: Edit cart
  @editcart
  Scenario: Check that the shopping cart page URL is correct
    Given I am on the shopping cart page
    Then The URL of the page is "https://magento.softwaretestingboard.com/checkout/cart/"
  @editcart
  Scenario: Remove item from the cart
    Given I am on the shopping cart page
    When I click the Remove item button
    Then I should see "You have no items in your shopping cart." message



