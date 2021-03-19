
#     ทดสอบการเข้าใช้งานของ "ขาย" (กรอกจำนวนและราคาขายเป็นทศนิยม)

import time
import unittest
import sys
from selenium import webdriver
from POM_test.login import *
from POM_test.sellingPage import *
from POM_test.scrollbar import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestSelling_18(unittest.TestCase):

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

            selling = SellingPage(driver)

            selling.into_sellingPage()

            time.sleep(2)

            selling.selling_crops_choose()

            time.sleep(2)

            selling.selling_marget_choose()

            time.sleep(2)

            selling.selling_value_totally("100.75")
            # กรอกจำนวนและราคาขายเป็นทศนิยม

            scroll.selling_scrolling()

            time.sleep(2)

            selling.selling_unit_choose()

            time.sleep(2)

            selling.selling_price_total("15000.2555")
            # กรอกจำนวนและราคาขายเป็นทศนิยม

            time.sleep(2)

            selling.selling_submit_finally()

            time.sleep(2)






        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()
