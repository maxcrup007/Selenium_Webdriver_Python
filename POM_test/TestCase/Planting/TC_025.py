
#     ทดสอบการเข้าใช้งานของ "ปลูก" (เลือกจำนวนค่าใช้จ่ายติดลบ)

import time
import unittest
import sys
from selenium import webdriver
from POM_test.login import *
from POM_test.plantPage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestPlanting_25(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            self.driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def test_login_valid(self):
            driver = self.driver

            self.driver.get("https://top-upstream-client.mulberrysoft.com/#/older/activity")

            login = LoginPage(driver)
            login.enter_username("demo005")
            login.enter_password("123456")
            login.click_login()

            time.sleep(2)

            plant = PlantPage(driver)
            plant.into_plantPage()
            plant.upload_picture()

            time.sleep(2)

            plant.next_function()

            time.sleep(2)

            plant.plant_enter_value("10")

            time.sleep(2)

            plant.plant_enter_area("10")

            time.sleep(2)

            plant.plant_enter_crops()

            time.sleep(2)

            # driver.find_element_by_xpath("//ion-list[2]/ion-item/ion-select").click()
            # driver.find_element_by_xpath("//button/div/div[2]").click()
            # driver.find_element_by_xpath("//button[2]/span").click()

            plant.plant_enter_garden()

            time.sleep(2)

            plant.plant_enter_unit()

            time.sleep(2)

            plant.plant_enter_area_unit()

            time.sleep(2)

            ########################################################################

            plant.plant_enter_products("100")

            time.sleep(2)

            plant.plant_enter_unit_products()

            time.sleep(2)

            plant.plant_enter_paid("-1500")
            # เลือกจำนวนค่าใช้จ่ายติดลบ

            time.sleep(2)

            plant.plant_enter_submit()

            time.sleep(2)



        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()
