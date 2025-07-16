Feature: automationexercise Login Functionality

  Scenario: Successful login with valid credentials
    Given I open the automationexercise login page in Edge
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to dashboard

  Scenario: Unsuccessful login with invalid credentials
    Given I open the automationexercise login page in Edge
    When I enter invalid credentials
    And I click the login button
    Then I should see a login error message