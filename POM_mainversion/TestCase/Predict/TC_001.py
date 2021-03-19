import time
import unittest
import sys
from selenium import webdriver
from POM_mainversion.login import *
from POM_mainversion.predictPage import *
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
            predict = PredictPage(driver)
            login.enter_username("demo003")
            login.enter_password("123456")
            login.click_login()

            time.sleep(2)

            login.click_interface()

            time.sleep(2)

            predict.into_predictPage()

            time.sleep(2)

            predict.select_marget()

            time.sleep(2)

            predict.upload_picture_predict()

            time.sleep(2)

            predict.select_predict_unit()

            time.sleep(2)

            predict.predict_enter_value("400")

            time.sleep(2)

            predict.predict_confirm_submit()

            time.sleep(2)


















        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()




