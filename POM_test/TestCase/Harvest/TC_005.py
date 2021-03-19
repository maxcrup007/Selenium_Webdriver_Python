
#     ทดสอบการเข้าใช้งานของ "เก็บเกี่ยว" (กรอกจำนวนที่เก็บเกี่ยวเป็นตัวอักษร)

import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from POM_test.login import *
from POM_test.harvestPage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestHarvest_5(unittest.TestCase):

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

            harvest = HarvestPage(driver)

            harvest.into_predictPage()

            time.sleep(2)

            harvest.upload_image()

            time.sleep(2)

            harvest.harvest_crops_choose()

            time.sleep(2)

            harvest.harvest_value_crops("one-hundred")
            # กรอกจำนวนที่เก็บเกี่ยวเป็นตัวอักษร

            time.sleep(2)

            scroll = driver.find_element_by_xpath("//ion-list[3]/ion-item/ion-input/input")
            action = ActionChains(driver)
            action.move_to_element(scroll).perform()
            # action object creation to scroll round 1

            harvest.harvest_unit_choose()

            time.sleep(2)

            harvest.harvest_paid_crops("1500")

            time.sleep(2)

            harvest.harvest_submit_totally()

            time.sleep(2)




        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()
