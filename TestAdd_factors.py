import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")

# Start and open browser
driver.get("https://top-upstream-client.mulberrysoft.com/")

# Log-in by username
driver.find_element_by_name("ion-input-0").send_keys("demo004")

# Log-in by password
driver.find_element_by_name("ion-input-1").send_keys("598745")


# Add click on the "Log in"
driver.find_element_by_css_selector(".ion-color").click()

time.sleep(5)

# Add click on the "เพิ่มกิจกรรม"
driver.find_element_by_css_selector(".ion-color-success").click()

# Add click on the "ปัจจัยการผลิด"
driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-farmer/ion-tabs/div/ion-router-outlet/app-activity-list/ion-content/section/ion-list/ion-item[1]").click()


time.sleep(5)



# driver.switch_to.default_content()

#### app-stock-form ###### ion-page #########

# driver.switch_to_frame(driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-modal/div/app-stock-form"))


# Upload Picture
driver.find_element_by_class_name("ion-color ion-color-warning md button button-large button-solid button-strong ion-activatable ion-focusable hydrated").send_keys("C://Users/voraw/Desktop/Picture/work/fr5.jpg")



# Choose a "หมวดหมู่"
element = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-modal/div/app-stock-form/ion-content/section[2]/form/ion-list/ion-item[2]/ion-select//button")
drop_down = Select(element)
drop_down.select_by_visible_text('ปุ๋ย')
driver.switch_to_alert().accept()


# Add a "ชื่อ"
driver.find_element_by_xpath("//ion-modal[@id='ion-overlay-2']/div/app-stock-form/ion-content/section[2]/form/ion-list/ion-item[3]/ion-input/input").send_keys("eiei")


# Add a "ปริมาณปัจจัย"
driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-modal/div/app-stock-form/ion-content/section[2]/form/ion-list/ion-item[4]/ion-input/input").send_keys("2")


# Choose a "ปริมาณปัจจัย"
element2 = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-modal/div/app-stock-form/ion-content/section[2]/form/ion-list/ion-item[4]/ion-select//button")
drop_down2 = Select(element2)
drop_down2.select_by_visible_text('กระสอบ')
driver.switch_to_alert().accept()


# Add a "ราคา"
driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-modal/div/app-stock-form/ion-content/section[2]/form/ion-list/ion-item[5]/ion-input/input").send_keys("500")


# Confirm an alert
driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-modal/div/app-stock-form/ion-content/section[2]/form/ion-button//button/span")
driver.switch_to_alert(By.CLASS_NAME, "alert-wrapper sc-ion-alert-md").accept(driver.find_element_by_css_selector(".ion-overlay-68"))

