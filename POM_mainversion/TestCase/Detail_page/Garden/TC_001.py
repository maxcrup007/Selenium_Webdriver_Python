import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from POM_mainversion.login import *
from POM_mainversion.Detail_page import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestGarden(unittest.TestCase):

        @classmethod
        def setUpClass(self):
            self.driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

        def test_login_valid(self):
            driver = self.driver

            self.driver.get("https://top-upstream-client.mulberrysoft.com")
            login = LoginPage(driver)
            garden = Detail_Garden_Page(driver)
            login.enter_username("demo004")
            login.enter_password("598745")
            login.click_login()

            time.sleep(2)

            login.click_interface()

            time.sleep(2)

            garden.into_garden()

            time.sleep(2)

            garden.upload_image_garden()

            time.sleep(2)

            scroll = driver.find_element_by_xpath("//ion-item[4]/ion-input/input")
            action = ActionChains(driver)
            action.move_to_element(scroll).perform()

            garden.garden_enter_unit()

            time.sleep(2)

            garden.name_garden_input("eiei")

            time.sleep(2)

            garden.number_garden_input("555")

            time.sleep(2)

            garden.area_garden_input("8")

            time.sleep(2)

            scroll2 = driver.find_element_by_xpath("//ion-item[10]/ion-select")
            action = ActionChains(driver)
            action.move_to_element(scroll2).perform()

            time.sleep(2)

            garden.garden_enter_owner()

            time.sleep(2)

            garden.garden_enter_district()

            time.sleep(2)

            garden.garden_enter_status()

            time.sleep(2)

            scroll3 = driver.find_element_by_xpath("//form/ion-button")
            action = ActionChains(driver)
            action.move_to_element(scroll3).perform()

            garden.garden_accept_submit()

            time.sleep(2)




            















        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()




