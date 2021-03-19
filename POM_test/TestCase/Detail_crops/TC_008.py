
#         ทดสอบการเข้าเพิ่มข้อมูลของ "แปลง" (ไม่เลือกทำรายการอะไรเลย)

import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from POM_test.login import *
from POM_test.crops_dataPage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestGarden_8(unittest.TestCase):

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

            crops = CropsPage(driver)

            crops.into_cropsDetail()

            time.sleep(2)

            # ไม่เลือกทำรายการอะไรเลย

            driver.find_element_by_xpath("//ion-list/ion-button").click()
            driver.find_element_by_xpath("//button[2]/span").click()

            time.sleep(2)






        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()
