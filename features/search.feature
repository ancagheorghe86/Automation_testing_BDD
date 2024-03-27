Feature: Search

  Background: Open home page
    Given I am on the home page
  @search
  Scenario: Search works properly for existing items
    When I enter "Dash" in the search field
    And I click the search button
    Then I am redirected to the search results page
    And There are some results displayed

