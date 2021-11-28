from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/Jon/OneDrive/Desktop/QA Automation/python-selenium-automation/chromedriver.exe')

# By XPATH Search Help Library input using contains for partial attr
driver.find_element(By.XPATH, "//input[@id='helpsearch']")


# By XPATH Search Help Library input using contains for partial attr
driver.find_element(By.ID, "//div[@class='a-search a-span12']")


# By XPATH search logo, maybe search button?
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-search']")

# By XPATH expected word next page
driver.find_element(By.XPATH, "//a[@class='cs-help-title']")


# By XPATH the whole search box
driver.find_element(By.XPATH, "//div[@class='a-section a-spacing-extra-large a-spacing-top-extra-large ss-landing-container-wide']")

