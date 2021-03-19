import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from selenium import webdriver
from POM.loginPage import *
from POM.homePage import *


class LoginTest(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            self.driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def test_login_valid(self):
            driver = self.driver

            self.driver.get("http://opensource-demo.orangehrmlive.com/")

            login = LoginPage(driver)
            login.enter_username("Admin")
            login.enter_password("admin123")
            login.click_login()

            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()

            time.sleep(2)
            # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
            # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
            # self.driver.find_element_by_id("btnLogin").click()
            # self.driver.find_element_by_id("welcome").click()
            # self.driver.find_element_by_link_text("Logout").click()
            time.sleep(2)

        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()


