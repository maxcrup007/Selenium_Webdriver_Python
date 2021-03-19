import time
import unittest
import sys
from selenium import webdriver
from selenium.webdriver import ActionChains
from POM_mainversion.login import *
from POM_mainversion.planingPage import *
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class TestGarden(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(
            executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        self.driver.get("https://top-upstream-client.mulberrysoft.com")
        login = LoginPage(driver)
        plan = PlaningPage(driver)
        login.enter_username("demo003")
        login.enter_password("123456")
        login.click_login()

        time.sleep(2)

        login.click_interface()

        time.sleep(2)

        plan.into_plan()

        time.sleep(2)

        plan.click_plan_button()

        time.sleep(2)

        plan.plan_garden_input()

        time.sleep(2)

        plan.plan_crops_input()

        time.sleep(2)

        plan.plan_enter_area("44")

        time.sleep(2)

        plan.plan_area_input()

        time.sleep(2)

        plan.plan_enter_amount("40")

        time.sleep(2)

        plan.plan_amount_input()

        time.sleep(2)

        plan.plan_enter_value("10000")

        time.sleep(2)

        plan.plan_value_input()

        time.sleep(2)

        scroll = driver.find_element_by_xpath("//form/ion-button")
        action = ActionChains(driver)
        action.move_to_element(scroll).perform()

        time.sleep(2)

        plan.plan_submit_confirm()

        time.sleep(2)

        plan.plan_saved_confirm()

        time.sleep(2)











    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

    if __name__ == '__main__':
        unittest.main()




