
#         ทดสอบการเข้าเพิ่มข้อมูลของ "แปลง" (ทำรายการยกเว้น กรอกพื้นที่แปลง)

import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from POM_test.login import *
from POM_test.garden_dataPage import *
from POM_test.scrollbar import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestGarden_11(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            self.driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def test_login_valid(self):
            driver = self.driver

            self.driver.get("https://top-upstream-client.mulberrysoft.com/#/older/activity")

            login = LoginPage(driver)
            scroll = ScrollbarPage(driver)
            login.enter_username("demo005")
            login.enter_password("123456")
            login.click_login()

            time.sleep(2)

            garden = GardenFiledPage(driver)

            garden.into_gardenDetail()

            time.sleep(5)

            garden.upload_image_garden()

            time.sleep(5)

            scroll.scrolling_garden_1()

            garden.garden_enter_unit()

            time.sleep(2)

            driver.find_element_by_name("ion-input-2").send_keys("eiei")

            time.sleep(2)

            driver.find_element_by_name("ion-input-3").send_keys("007")

            time.sleep(2)

            # driver.find_element_by_name("ion-input-7").send_keys("4") (ทำรายการยกเว้น กรอกพื้นที่แปลง)

            time.sleep(2)

            scroll.scrolling_garden_2()

            garden.garden_enter_owner()

            time.sleep(2)

            garden.garden_enter_district()

            time.sleep(2)

            driver.find_element_by_name("ion-input-5").send_keys("555")

            time.sleep(2)

            garden.garden_enter_status()

            time.sleep(5)

            scroll.scrolling_garden_3()

            driver.find_element_by_xpath("//form/ion-button").click()
            driver.find_element_by_xpath("//button[2]/span").click()

            time.sleep(2)














        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()
