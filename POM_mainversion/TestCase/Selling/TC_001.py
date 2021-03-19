import time
import unittest
import sys
from selenium import webdriver
from POM_mainversion.login import *
from POM_mainversion.sellingPage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestSelling_1(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            self.driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def test_login_valid(self):
            driver = self.driver

            self.driver.get("https://top-upstream-client.mulberrysoft.com")
            login = LoginPage(driver)
            selling = SellingPage(driver)
            login.enter_username("demo003")
            login.enter_password("123456")
            login.click_login()

            time.sleep(2)

            login.click_interface()

            time.sleep(2)

            selling.into_sellingPage()

            time.sleep(2)

            selling.select_marget_picture()

            time.sleep(2)

            selling.selling_enter_value("50")

            time.sleep(2)

            selling.select_unit_selling()

            time.sleep(2)

            selling.selling_enter_paid("500")

            time.sleep(2)

            selling.selling_enter_price("5000")

            time.sleep(2)

            selling.selling_enter_menu("eiei")

            time.sleep(2)

            selling.selling_enter_prices("5000")

            time.sleep(2)

            selling.selling_confirm_submit()

            time.sleep(2)




















        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()




