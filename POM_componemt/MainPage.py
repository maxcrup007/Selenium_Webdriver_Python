import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from selenium import webdriver
from POM_componemt.page import *
from POM_componemt.homePage import *


class TestLogin(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            self.driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def test_login_valid(self):
            driver = self.driver

            self.driver.get("http://testautomationpractice.blogspot.com/")
            self.driver.switch_to_frame("frame-one1434677811")
            time.sleep(5)

            login = LoginPage(driver)
            login.enter_first_name("demo004")
            login.enter_last_name("eiei")
            login.enter_phone("0888888")

            time.sleep(2)

            login.enter_country("Thailand")
            login.enter_city("Chiang rai")

            time.sleep(2)

            self.driver.find_element_by_name("RESULT_FileUpload-10").send_keys("D:/images.jpg")
            login.click_submit()

            time.sleep(2)

            # homepage = HomePage(driver)
            # homepage.click_welcome()



            # homepage.click_editprofile()



            # homepage.click_welcome()



            # homepage.click_logout()



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