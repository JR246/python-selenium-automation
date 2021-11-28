from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/Jon/OneDrive/Desktop/QA Automation/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-extra-large a-spacing-top-extra-large ss-landing-container-wide']").send_keys('cancel order')

driver.find_element(By.ID, "//input[@id='helpsearch']").click()

actual_result = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-search']")
expected_result = '"cancel order"'

assert actual_result == expected_result, f'Error, actual {actual_result} did not watch {expected_result}'

print('Test case passed')
driver.quit()