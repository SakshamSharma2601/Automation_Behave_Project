from driver_setup import start_edge
from behave import *
import time
from selenium.webdriver.common.by import By

@given('I open the automationexercise home page in Edge')
def step_impl(context):
    context.driver = start_edge()
    context.driver.maximize_window()
    context.driver.get("https://automationexercise.com/")
    time.sleep(2)

@when('I navigate to a product and select product options in it')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']").click()
    time.sleep(1)

@when('I add the product to cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']").click()
    time.sleep(2)

@then('The product should be added to the cart')
def step_impl(context):
    assert "Your product has been added to cart" in context.driver.page_source
    
@when('I navigate to cart options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//u[normalize-space()='View Cart']").click()
    time.sleep(1)

@when('I remove the product from the cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[@class='cart_quantity_delete']").click()
    time.sleep(1)
    
@then(u'The cart should be empty')
def step_impl(context):
    assert "Cart is empty" in context.driver.page_source