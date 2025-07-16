Feature: Checkout Functionality on AutomationExercise

  Background: User ready to checkout
    Given I am logged in as a registered user
    And I have added at least one product to the cart
    When I click on "Proceed to Checkout"

  Scenario: Verify checkout page UI elements
    Then I should see the delivery address, the billing address section and Place order button

  Scenario: I place an order with valid payment details and it is success
    When I click on the PLACE ORDER button
    When I fill in account details and submit
    Then I should see a confirmation message like "Congratulations! Your order has been confirmed!"

  Scenario: Download invoice and return to homepage after placing the order
    When I click on the PLACE ORDER button
    When I fill in account details and submit
    And I click on the "Download Invoice" button
    And I click on the "Continue" button
    Then I should be redirected to the homepage

  Scenario: Verify cart is empty after successful order
    When I place a complete order and return to cart
    And I navigate to the cart page
    Then the cart should be empty with a message like "Cart is empty"