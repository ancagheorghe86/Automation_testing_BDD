Feature: Add to cart
  @cart
  Scenario: Check that the search results page URL is correct
    Given I am on the search results page
    Then The URL of the page is "https://magento.softwaretestingboard.com/catalogsearch/result/?q=dash"
  @cart
  Scenario: Add to cart
    Given I am on the search results page
    When I click the watch I want
    When I click add to cart
    Then Cart not empty


