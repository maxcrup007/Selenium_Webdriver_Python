import time
import unittest
import sys
from selenium import webdriver
from POM_mainversion.login import *
from POM_mainversion.Detail_page import *
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
            crops = Detail_Crops_Page(driver)
            login.enter_username("demo003")
            login.enter_password("123456")
            login.click_login()

            time.sleep(2)

            login.click_interface()

            time.sleep(2)

            crops.into_crops()

            time.sleep(2)

            crops.choose_category()

            time.sleep(2)

            crops.choose_crops()

            time.sleep(2)

            crops.choose_standard()

            time.sleep(2)

            crops.click_submit_confirm()

            time.sleep(2)











        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()




