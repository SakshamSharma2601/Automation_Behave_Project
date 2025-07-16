from driver_setup import start_edge
from behave import *
import time
from selenium.webdriver.common.by import By

EXISTING_PRODUCT = "top" 
NON_EXISTING_PRODUCT = "productdoesnotexist12345"

@given('I open the automationexercise product search in Edge')
def step_impl(context):
    context.driver = start_edge()
    context.driver.get("https://automationexercise.com/products")
    time.sleep(2)

@when('I enter the existing product name')
def step_impl(context):
    context.driver.find_element(By.ID, "search_product").send_keys(EXISTING_PRODUCT)

@when('I enter a non-existing product name into the search box')
def step_impl(context):
    context.driver.find_element(By.ID, "search_product").send_keys(NON_EXISTING_PRODUCT)

@when('I leave the search box empty')
def step_impl(context):
    context.driver.find_element(By.ID, "search_product").clear()

@when('I click the search button')
def step_impl(context):
    context.driver.find_element(By.ID, "submit_search").click()
    time.sleep(2)

@then('Searched product should be displayed in the search results')
def step_impl(context):
    products = context.driver.find_elements(By.CLASS_NAME, "product-image-wrapper")
    assert len(products) > 0, "Product not found in search results"
    context.driver.quit()

@then('I should see a message indicating that no products were found')
def step_impl(context):
    if "No Products Found" not in context.driver.page_source:
        context.driver.save_screenshot("screenshots/no_products_found_bug.png")
        assert False, "Expected Message not found"
    context.driver.quit()

@then('I should see a message indicating that search input is required')
def step_impl(context):
    if "Search Input Required" not in context.driver.page_source:
        context.driver.save_screenshot("screenshots/search_input_req_bug.png")
        assert False, "Expected Message not found"
    context.driver.quit()