from driver_setup import start_edge
import time
from behave import *
from selenium.webdriver.common.by import By

EMAIL = "TestUSER253448@example.com"
INVALID_EMAIL = "invalid-email-format.com"

def common_fields(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("TestUser")

@given('I open the automationexercise registration page in Edge')
def step_impl(context):
    context.driver = start_edge()
    context.driver.maximize_window()
    context.driver.get("https://automationexercise.com/login")
    time.sleep(3)

@when('I enter valid registration details')
def step_impl(context):
    common_fields(context)
    context.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(EMAIL)

@when('I click signup button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[text()='Signup']").click()

@when('I fill in all required details')
def step_impl(context):
    context.driver.find_element(By.ID, "id_gender1").click()
    context.driver.find_element(By.ID, "password").send_keys("Test1234")
    context.driver.find_element(By.ID, "days").send_keys("10")
    context.driver.find_element(By.ID, "months").send_keys("May")
    context.driver.find_element(By.ID, "years").send_keys("2000")
    context.driver.find_element(By.ID, "first_name").send_keys("John")
    context.driver.find_element(By.ID, "last_name").send_keys("Doe")
    context.driver.find_element(By.ID, "address1").send_keys("123 Test St")
    context.driver.find_element(By.ID, "country").send_keys("United States")
    context.driver.find_element(By.ID, "state").send_keys("Minnesota")
    context.driver.find_element(By.ID, "city").send_keys("Downtown")
    context.driver.find_element(By.ID, "zipcode").send_keys("175441")
    context.driver.find_element(By.ID, "mobile_number").send_keys("9876543210")

@when('I click "Create Account"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

@then('I should see a success message "ACCOUNT CREATED!"')
def step_impl(context):
    assert "Account Created!" in context.driver.page_source
    context.driver.quit()

@when('I enter existing email in the registration form')
def step_impl(context):
    common_fields(context)
    context.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(EMAIL)

@then('I should see an error "Email Address already exist!"')
def step_impl(context):
    assert "Email Address already exist" in context.driver.page_source
    context.driver.quit()

@when('I enter registration details')
def step_impl(context):
    common_fields(context)
    context.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("TestUS34748@example.com")

@when('I leave required fields empty and click "Create Account"')
def step_impl(context):
    context.driver.find_element(By.ID, "id_gender1").click()
    context.driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

@then('I should see validation errors for missing fields')
def step_impl(context):
    assert "required" in context.driver.page_source.lower() or "error" in context.driver.page_source.lower()
    context.driver.quit()
























