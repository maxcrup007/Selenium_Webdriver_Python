import time
import unittest
import sys
from selenium import webdriver
from POM_mainversion.login import *
from POM_mainversion.preparePage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestLogin(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            self.driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def test_login_valid(self):
            driver = self.driver

            self.driver.get("https://top-upstream-client.mulberrysoft.com")
            login = LoginPage(driver)
            prepare = PreparePage(driver)
            login.enter_username("demo003")
            login.enter_password("123456")
            login.click_login()

            time.sleep(2)

            login.click_interface()

            time.sleep(2)

            prepare.into_preparePage()

            time.sleep(2)

            prepare.choose_category_prepare()

            time.sleep(2)

            prepare.directory_prepare()

            time.sleep(2)

            prepare.prepare_enter_menu("eiei")

            time.sleep(2)

            prepare.prepare_enter_price("5000")

            time.sleep(2)














        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()




