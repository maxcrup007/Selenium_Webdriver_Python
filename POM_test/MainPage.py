import time
import unittest
import sys
from selenium import webdriver
from POM_test.login import *
from POM_test.homePage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class Test_TOP(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            self.driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def test_login_valid(self):
            driver = self.driver

            self.driver.get("https://top-upstream-client.mulberrysoft.com/")

            login = LoginPage(driver)
            login.enter_username("demo004")
            login.enter_password("598745")
            login.click_login()
            homepage = HomePage(driver)
            homepage.click_welcome()

            time.sleep(2)

            homepage.click_editprofile()


            time.sleep(2)

            homepage.click_welcome()

            time.sleep(2)

            homepage.click_logout()

            time.sleep(2)



        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()


# class TestEdit(unittest.TestCase):
#
#         @classmethod
#         def setUpClass(self):
#             self.driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
#             self.driver.implicitly_wait(10)
#             self.driver.maximize_window()
#
#         def test_edit_profile(self):
#             driver = self.driver
#
#             self.driver.get("https://top-upstream-client.mulberrysoft.com/")
#
#             login = LoginPage(driver)
#             login.enter_username("demo004")
#             login.enter_password("598745")
#             login.click_login()
#             homepage = HomePage(driver)
#             homepage.click_welcome()
#
#             time.sleep(2)
#
#             homepage.click_editprofile()
#
#             time.sleep(2)
#
#             # EditProfile.enter_first_name("วชิรพงษ์ มหาโชติ")
#             # EditProfile.enter_email("wachirapong@gmail.com")
#             # EditProfile.enter_phone_number("0915767825")
#             # EditProfile.enter_address("555")
#
#             time.sleep(2)
#
#             homepage.click_welcome()
#
#             time.sleep(2)
#
#             homepage.click_logout()
#
#         @classmethod
#         def tearDownClass(cls):
#             cls.driver.close()
#             cls.driver.quit()
#             print("Test Completed")
#
#         if __name__ == '__main__':
#             unittest.main()