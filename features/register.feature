Feature: automationexercise Account Registration

  Background:
    Given I open the automationexercise registration page in Edge

  Scenario: Successfull Account registration with valid details
    When I enter valid registration details
    And I click signup button
    When I fill in all required details
    And I click "Create Account"
    Then I should see a success message "ACCOUNT CREATED!"

  Scenario: Registration with Existing Email
    When I enter existing email in the registration form
    And I click signup button
    Then I should see an error "Email Address already exist!"

  Scenario: Registration with Missing Required Fields
    When I enter registration details
    And I click signup button
    When I leave required fields empty and click "Create Account"
    Then I should see validation errors for missing fields
