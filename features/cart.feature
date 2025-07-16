
Feature: Cart Functionality
    
  Background: Common Steps
    Given I open the automationexercise home page in Edge
    When I navigate to a product and select product options in it
    And I add the product to cart

  Scenario: Add product to cart
    Then The product should be added to the cart

  Scenario: Remove product from cart
    When I navigate to cart options
    And I remove the product from the cart
    Then The cart should be empty

