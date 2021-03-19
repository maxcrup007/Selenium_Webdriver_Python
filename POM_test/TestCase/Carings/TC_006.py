
#     ทดสอบการเข้าใช้งานของ "ดูแล" (แต่ไม่กรอกอะไรเลย)

import time
import unittest
import sys
from selenium import webdriver
from POM_test.login import *
from POM_test.carePage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestCarring_6(unittest.TestCase):

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

            care = CarePage(driver)

            care.into_caringPage()

            time.sleep(2)

            care.upload_picture()

            time.sleep(2)

            # care.care_choose_plant()
            #
            # time.sleep(2)
            #
            # care.care_enter_paid("1500")

            # (แต่ไม่กรอกอะไรเลย)

            time.sleep(2)

            care.submit_confirm_care()

            time.sleep(2)






        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()
