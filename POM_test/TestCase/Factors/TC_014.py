
#     ทดสอบการเข้าใช้งานของ "ปัจจัย" (เลือกหน่วยให้ไม่ตรงกับชนิดปัจจัย)

import time
import unittest
import sys
from selenium import webdriver
from POM_test.login import *
from POM_test.factorPage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestFactor_14(unittest.TestCase):

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

            factor = FactorPage(driver)
            factor.into_factorPage()
            factor.upload_picture()

            time.sleep(2)

            factor.next_function()

            time.sleep(2)

            factor.factor_enter_name("ปุ๋ยอิอิ")

            time.sleep(2)

            factor.factor_enter_value("10")

            time.sleep(2)

            factor.factor_enter_price("1000")

            time.sleep(2)

            factor.factor_enter_category() # (เลือกหน่วยให้ไม่ตรงกับชนิดปัจจัย)
            factor.factor_enter_unit()
            factor.factor_enter_confirm()


            time.sleep(3)

            factor.factor_confirm()




        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()
