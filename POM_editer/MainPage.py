import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from selenium import webdriver
from POM_editer.login import *
from POM_editer.interface import *
from POM_editer.EditProfile import *


class TestLogin(unittest.TestCase):

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

            edit_profile = EditProfile(driver)

            edit_profile.enter_first_name().clear()
            edit_profile.enter_first_name("eiei")
            edit_profile.enter_phone_number().clear()
            edit_profile.enter_phone_number("088888")
            edit_profile.enter_email().clear()
            edit_profile.enter_email("demo004@GMAIL.COM")
            edit_profile.enter_address().clear()
            edit_profile.enter_address("555")


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
