
#     ทดสอบการเข้าใช้งานของ "ข้อมูลส่วนตัว" (กรอกจำนวนที่ประเมินเป็นค่าติดลบ)

import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from POM_test.login import *
from POM_test.profilePage import *
from POM_test.scrollbar import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestProfile_8(unittest.TestCase):

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

            profile = ProfilePage(driver)

            profile.into_profilePage()

            time.sleep(5)

            profile.profile_name_input("วัชรพงษ์ มหาโชติ")

            time.sleep(2)

            profile.profile_email_input("vatcharapong11@hotmail.com")

            time.sleep(2)

            profile.profile_phone_number("086799315")

            time.sleep(2)

            scroll.profile_scrolling()

            time.sleep(2)

            profile.profile_address_text("-125 5858 ^&_*&$%")

            time.sleep(2)

            scroll.profile_scrolling2()

            time.sleep(2)

            profile.profile_submit_confirm()

            time.sleep(2)


        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()
