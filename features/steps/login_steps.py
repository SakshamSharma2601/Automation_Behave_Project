from driver_setup import start_edge
import time
from behave import *
from selenium.webdriver.common.by import By

EMAIL= "TestUSER253448@example.com"
PASSWORD = "Test1234"

@given('I open the automationexercise login page in Edge')
def step_impl(context):
    context.driver = start_edge()
    context.driver.maximize_window()
    context.driver.get("https://automationexercise.com/login")
    time.sleep(2)

@when('I enter valid credentials')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(EMAIL) 
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(PASSWORD)

@when('I enter invalid credentials')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("wronguser@example.com")
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("wrongpassword")

@when('I click the login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(3)

@then('I should be redirected to dashboard')
def step_impl(context):
    time.sleep(3)  # give the page time to load
    assert context.driver.current_url == "https://automationexercise.com/"
    context.driver.quit()
    
@then('I should see a login error message')
def step_impl(context):
    assert "Your email or password is incorrect" in context.driver.page_source 
    context.driver.quit()

