
#     ทดสอบการเข้าใช้งานของ "ปัจจัย"

import time
import unittest
import random
import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from POM_mainversion.login import *
from POM_mainversion.factorPage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestPlanting_1(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            self.driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def test_login_valid(self):
            driver = self.driver

            self.driver.get("https://top-upstream-client.mulberrysoft.com")

            login = LoginPage(driver)
            login.enter_username("demo003")
            login.enter_password("123456")
            login.click_login()

            time.sleep(2)

            factors = FactorPage(driver)
            factors.into_factorPage()

            time.sleep(2)

            factors.upload_picture_factor()

            time.sleep(2)

            scroll = driver.find_element_by_xpath("//ion-item[5]/ion-input/input")
            action = ActionChains(driver)
            action.move_to_element(scroll).perform()

            time.sleep(2)

            factors.choose_category_factors()

            time.sleep(2)

            names = ["eiei", "sawatdeekrub", "thanphujaroen"]

            select_name = random.choice(names)

            factors.factor_enter_name(select_name)

            time.sleep(2)

            scroll = driver.find_element_by_xpath("//ion-item[5]/ion-input/input")
            action = ActionChains(driver)
            action.move_to_element(scroll).perform()

            factors.factor_enter_value("500")

            time.sleep(2)

            factors.factor_enter_unit()

            time.sleep(2)

            factors.factor_enter_price("1500")

            time.sleep(2)

            scroll = driver.find_element_by_xpath("//form/ion-button")
            action = ActionChains(driver)
            action.move_to_element(scroll).perform()

            factors.factor_submit_complete()

            time.sleep(2)












        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()
