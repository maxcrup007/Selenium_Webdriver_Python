from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://top-upstream-client.mulberrysoft.com/")

# assert "Welcome: Thai Organic Platform" in driver.title

driver.find_element_by_name("ion-input-0").send_keys("demo003")
driver.find_element_by_name("ion-input-1").send_keys("123456")

driver.find_element_by_css_selector(".ion-color").click()


# Start and open browser
