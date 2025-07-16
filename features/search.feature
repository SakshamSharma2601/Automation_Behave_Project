Feature: automationexercise search Functionality

  Background:
    Given I open the automationexercise product search in Edge

  Scenario: Validate searching with an existing Product Name
    When I enter the existing product name
    And I click the search button
    Then Searched product should be displayed in the search results

  Scenario: Validate searching with a non-existing product name
    When I enter a non-existing product name into the search box
    And I click the search button
    Then I should see a message indicating that no products were found
  # No message displayed, and default product grid is shown


  Scenario: Search with empty input should show validation
    When I leave the search box empty
    And I click the search button
    Then I should see a message indicating that search input is required
  # no message shown - log as a bug for test project
