from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")

driver.get("https://top-upstream-client.mulberrysoft.com/")

user_element = driver.find_element_by_name("ion-input-0")


print(user_element.is_displayed())

print(user_element.is_enabled())


password_element = driver.find_element_by_name("ion-input-1")

user_element.send_keys("demo004")

password_element.send_keys("598745")


driver.find_element_by_css_selector(".ion-color").click()








