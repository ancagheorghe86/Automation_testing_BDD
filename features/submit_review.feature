Feature: Submit a review
  @submit
  Scenario: Verify watch model URL
    Given I am on the watch model URL
    Then The URL ofe the page is "https://magento.softwaretestingboard.com/dash-digital-watch.html"
  @submit
  Scenario: Submit a review
    Given I am on the watch model URL
    When I click the Reviews button
    When I set the Nickname
    When I set the Summary
    When I set the Review
    When I set one star rating
    When I click on Submit Review button
    Then I should see "You submitted your review for moderation." message

