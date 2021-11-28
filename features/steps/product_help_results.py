from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Search results for Cancel Items or Orders')
def verify_search_result(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1")
    expected_result = 'Cancel Items or Orders'
    assert actual_result.text == expected_result, f'Eroor, actual {actual_result} did not cancel order {expected_result}'