from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
# driver = webdriver.Firefox(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/FirefoxDriver/FirefoxDriver")
driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")

driver.get("https://top-upstream-client.mulberrysoft.com/")


print(driver.title)
print(driver.current_url)

driver.close()
