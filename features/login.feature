Feature: Login Page

  Scenario: Check that the URL is correct
    Given I am on the login page
    Then  The URL of the page is "https://magento.softwaretestingboard.com/customer/account/login"


  Scenario Outline: Log in with unregistered email
    Given I am on the login page
    When I enter "<email>" as email
    And I enter "<password>" as password
    And I click the login button
    Then I should see "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later." message
    Examples:
      | email             | password      |
      | gina88@gmail.com  | ginaginuta    |
      | ginel99@ymail.com | ginelginel123 |










