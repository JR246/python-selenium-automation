from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/Jon/OneDrive/Desktop/QA Automation/python-selenium-automation/chromedriver.exe')


#By.XPATH Amazon Logo
driver.find_element(By.XPATH, "//a[@href='/ref=ap_frn_logo']")

#By.ID Email Field
driver.find_element(By.ID, "//input[@id='ap_email']")

#By.ID Contiue Button
driver.find_element(By.XPATH, "//span[@class='a-button-inner']//input[@id='continue']")

#By.XPATH Need help Link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#By.ID Forgot your password Link
driver.find_element(By.ID, "//a[@id= 'auth-fpp-link-bottom']")

#By.ID Other Issues with sign in Link
driver.find_element(By.ID, "//a[@id= 'ap-other-signin-issues-link']")

#By.ID Create your Amazon account button
driver.find_element(By.ID, "//a[@id='createAccountSubmit']")

#By.XPATH Conditions of Use Link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#By.XPATH Privacy Notice Link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
