from driver_setup import start_edge
import time
from behave import *
from selenium.webdriver.common.by import By

EMAIL= "TestUSER253448@example.com"
PASSWORD = "Test1234"

@given('I am logged in as a registered user')
def step_impl(context):
    context.driver = start_edge()
    context.driver.get("https://automationexercise.com/login")
    context.driver.find_element(By.NAME, "email").send_keys(EMAIL)
    context.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    context.driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)
    assert "Logged in as" in context.driver.page_source
    
@given('I have added at least one product to the cart')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']").click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Add to cart']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//u[normalize-space()='View Cart']").click()
    time.sleep(1)

@when('I click on "Proceed to Checkout"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.check_out").click()
    time.sleep(1)

@then('I should see the delivery address, the billing address section and Place order button')
def step_impl(context):
    assert "Your delivery address" in context.driver.page_source, "Delivery address section missing"
    assert "Your delivery address" in context.driver.page_source, "Billing address section missing"
    assert context.driver.find_element(By.XPATH, "//a[text()='Place Order']").is_displayed()
    context.driver.quit()

@when('I click on the PLACE ORDER button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Place Order']").click()
    time.sleep(2)

@when('I fill in account details and submit')
def step_impl(context):
    context.driver.find_element(By.NAME, "name_on_card").send_keys("Valid User")
    context.driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")
    context.driver.find_element(By.NAME, "cvc").send_keys("123")
    context.driver.find_element(By.NAME, "expiry_month").send_keys("12")
    context.driver.find_element(By.NAME, "expiry_year").send_keys("2026")
    time.sleep(1)
    context.driver.find_element(By.ID, "submit").click()
    time.sleep(2)


@then('I should see a confirmation message like "Congratulations! Your order has been confirmed!"')
def step_impl(context):
    assert "Congratulations! Your order has been confirmed!" in context.driver.page_source
    context.driver.quit()

@when('I click on the "Download Invoice" button')
def step_impl(context):
    invoice_button = context.driver.find_element(By.XPATH, "//a[text()='Download Invoice']")
    assert invoice_button.is_displayed(), "Download Invoice button not found"
    invoice_button.click()
    time.sleep(2)

@when('I click on the "Continue" button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Continue']").click()
    time.sleep(2)

@then('I should be redirected to the homepage')
def step_impl(context):
    assert context.driver.current_url == "https://automationexercise.com/", "Not redirected to homepage"
    context.driver.quit()

@when('I place a complete order and return to cart')
def step_impl(context):
    context.execute_steps('''
        When I click on the PLACE ORDER button
        And I fill in account details and submit
        And I click on the "Continue" button
    ''')

@when('I navigate to the cart page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[normalize-space()='Cart']").click()
    time.sleep(2)

@then('the cart should be empty with a message like "Cart is empty"')
def step_impl(context):
    page_text = context.driver.page_source.lower()
    assert "cart is empty" in page_text or "cart is empty!" in page_text, "Cart is not empty after order"
    context.driver.quit()