import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")


driver.get("https://top-upstream-client.mulberrysoft.com/")

driver.find_element_by_name("ion-input-0").send_keys("demo004")
driver.find_element_by_name("ion-input-1").send_keys("598745")



driver.find_element_by_css_selector(".ion-color").click()

time.sleep(5)

driver.find_element_by_css_selector(".ion-color-success").click()


links = driver.find_element(By.TAG_NAME, "h3")

print("Number of links present:", len(links))

for link in links:
    print(link.text)

