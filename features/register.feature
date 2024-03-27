Feature: Register page

  Scenario: Register new account
    Given I am on the register page
    Then  The URL of the page is "https://magento.softwaretestingboard.com/customer/account/create/"

  @regression
  Scenario: Register new account
    Given I am on the register page
    When I enter first name
    When I enter last name
    When I enter email
    When I enter password
    When I confirm password
    When I click the register button
    Then I should be logged in


