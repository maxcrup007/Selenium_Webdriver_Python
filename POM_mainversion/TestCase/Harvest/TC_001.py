import time
import unittest
import sys
from selenium import webdriver
from POM_mainversion.login import *
from POM_mainversion.harvestPage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestHarvest_1(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            self.driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def test_login_valid(self):
            driver = self.driver

            self.driver.get("https://top-upstream-client.mulberrysoft.com")
            login = LoginPage(driver)
            harvest = HarvestPage(driver)
            login.enter_username("demo003")
            login.enter_password("123456")
            login.click_login()

            time.sleep(2)

            login.click_interface()

            time.sleep(2)

            harvest.into_harvestPage()

            time.sleep(2)

            harvest.select_device()

            time.sleep(2)

            harvest.harvest_enter_menu("eiei")

            time.sleep(2)

            harvest.harvest_enter_price("4000")

            time.sleep(2)

            harvest.harvest_enter_value("50")

            time.sleep(2)

            harvest.harvest_selection()

            time.sleep(2)

            harvest.harvest_delete_input("500")

            time.sleep(2)

            harvest.harvest_keep_input("500")

            time.sleep(2)

            harvest.harvest_confirm_submit()

            time.sleep(2)























        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()




