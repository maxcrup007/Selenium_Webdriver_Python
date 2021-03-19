from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")

driver.get("https://www.google.co.th/")

print(driver.title)

driver.get("https://top-upstream-client.mulberrysoft.com/")

time.sleep(0)

print(driver.title)

driver.back()

time.sleep(0)

print(driver.title)

driver.forward()

time.sleep(0)

print(driver.title)

