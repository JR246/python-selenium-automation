from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('Open Amazon Help page')
def search_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Search for search field')
def search_amazon(context):
    element= context.driver.find_element(By.ID, "helpsearch")
    element.send_keys('cancel order')
    element.send_keys(Keys.ENTER)




#@when('Click on search icon in search page')
#def click_search_icon(context):
    #context.driver.find_element(By.ID, "//input[@id='helpsearch']").click()

