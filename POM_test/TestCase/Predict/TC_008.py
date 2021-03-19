
#     ทดสอบการเข้าใช้งานของ "ประเมิน" (กรอกจำนวนที่ประเมินเป็นทศนิยม)

import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from POM_test.login import *
from POM_test.predictPage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestPredict_8(unittest.TestCase):

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

            predict = PredictPage(driver)

            predict.into_predictPage()

            time.sleep(2)

            predict.upload_image()

            time.sleep(2)

            predict.predict_plant()

            time.sleep(2)

            predict.predict_select()

            time.sleep(2)

            predict.predict_value_selected("100.75")
            # กรอกจำนวนที่ประเมินเป็นทศนิยม

            time.sleep(2)

            scroll = driver.find_element_by_xpath("//ion-item[2]/ion-select")
            action = ActionChains(driver)
            action.move_to_element(scroll).perform()
            # action object creation to scroll round 1

            predict.predict_unit_selected()

            time.sleep(2)

            predict.predict_submit_value()

            time.sleep(2)




        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()
