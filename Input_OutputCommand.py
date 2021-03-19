import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")


driver.get("https://top-upstream-client.mulberrysoft.com/")
driver.find_element_by_name("ion-input-0").send_keys("demo004")
driver.find_element_by_name("ion-input-1").send_keys("598745")



driver.find_element_by_css_selector(".ion-color").click()


time.sleep(5)


driver.find_element_by_css_selector("#tab-button-menu > .md:nth-child(1)").click()
driver.find_element_by_css_selector(".item:nth-child(2) h3").click()

time.sleep(5)


driver.find_element_by_xpath("//ion-segment-button[@value='garden']").click()
driver.find_element_by_xpath("//ion-button[contains(.,'เพิ่มแปลง')]").click()

time.sleep(5)

driver.find_element_by_xpath("//ion-modal[@id='ion-overlay-5']/div/app-modal-garden/ion-content/section[2]/form/ion-list/ion-item/ion-input/input").send_keys("แปลงไงอิอิ1")







# Inputboxes = driver.find_element(By.CLASS_NAME, 'native-input sc-ion-input-md')
# print(len(Inputboxes))





# driver.find_element_by_xpath("//ion-modal[@id='ion-overlay-5']/div/app-modal-garden/ion-content/section/app-upload-image/ion-button").click()

