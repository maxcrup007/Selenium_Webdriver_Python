
#         ทดสอบการเข้าเพิ่มข้อมูลของ "แปลง" (ทำรายการยกเว้น การเลือกมาตราฐาน)

import time
import unittest
import sys
from selenium import webdriver
from POM_test.scrollbar import *
from selenium.webdriver.common.keys import Keys
from POM_test.login import *
from POM_test.garden_dataPage import *
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class TestGarden_6(unittest.TestCase):

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

            garden = GardenFiledPage(driver)

            garden.into_gardenDetail()

            time.sleep(5)

            garden.upload_image_garden()

            time.sleep(5)

            scroll.scrolling_garden_1()

            garden.garden_enter_unit()

            time.sleep(2)

            driver.find_element_by_name("ion-input-2").send_keys("eiei")

            time.sleep(2)

            driver.find_element_by_name("ion-input-3").send_keys("007")

            time.sleep(2)

            driver.find_element_by_name("ion-input-7").send_keys("4")

            time.sleep(2)

            scroll.scrolling_garden_2()

            garden.garden_enter_owner()

            time.sleep(2)

            garden.garden_enter_district()

            time.sleep(2)

            driver.find_element_by_name("ion-input-5").send_keys("555")

            time.sleep(2)

            garden.garden_enter_status()

            time.sleep(5)

            # ทำรายการยกเว้น การเลือกมาตราฐาน

            scroll.scrolling_garden_3()

            driver.find_element_by_xpath("//form/ion-button").click()
            driver.find_element_by_xpath("//button[2]/span").click()

            time.sleep(2)










        # def check2(driver, slidebar, sliderknob, percent):
        #
        #     height = slidebar.size['height']
        #     width = slidebar.size['width']
        #
        #     move = ActionChains(driver)
        #     # slidebar = driver.find_element_by_xpath("//div[@id='slider']/a")
        #
        #     if width > height:
        #         # highly likely a horizontal slider
        #         print("off set: ", percent * width / 100)
        #         move.click_and_hold(sliderknob).move_by_offset(500, 0).release().perform()
        #     else:
        #         # highly likely a vertical slider
        #         move.click_and_hold(sliderknob).move_by_offset(percent * height / 100, 0).release().perform()
        #
        #     driver.switch_to_default_content()
        #
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--no-proxy-server')
        #
        # os.environ["PATH"] += ":/home/mike/software"
        #
        # os.environ["PATH"] += ":/usr/local/bin/"
        #
        #
        # try:
        #     driver = webdriver.Chrome()
        #     driver.get("http://99.243.40.11/#/HouseSold")
        #     els = driver.find_elements_by_xpath('//input[@class="input high"]')
        #     print('els.len = ', len(els))
        #     e = els[0]
        #     ens = driver.find_elements_by_xpath('//span[@class="pointer high"]')
        #     en = ens[0]
        #     check2(driver, e, en, 70)
        #     time.sleep(20)
        # finally:
        #     driver.close()





        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
            print("Test Completed")

        if __name__ == '__main__':
            unittest.main()
