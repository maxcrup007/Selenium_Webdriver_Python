import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# /html/body/app-root/ion-app/ion-router-outlet/app-farmer/ion-tabs/div/ion-router-outlet/app-profile/ion-content/section[1]/app-upload-image/ion-button

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")

    def test_login(self):
        driver = self.driver

        # Start and open browser
        driver.get("https://top-upstream-client.mulberrysoft.com/")
        self.assertIn("Thai Organic Platform", driver.title)

        # Log-in by username
        driver.find_element_by_name("ion-input-0").send_keys("demo004")

        # Log-in by password
        driver.find_element_by_name("ion-input-1").send_keys("598745")

        # Add click on the "Log in"
        driver.find_element_by_css_selector(".ion-color").click()

        time.sleep(5)

        assert "No results found." not in driver.page_source


    def test_factor1(self):
        driver = self.driver
                                                      
        # Start and open browser
        driver.get("https://top-upstream-client.mulberrysoft.com/")
        self.assertIn("Thai Organic Platform", driver.title)

        # Log-in by username
        driver.find_element_by_name("ion-input-0").send_keys("demo004")

        # Log-in by password
        driver.find_element_by_name("ion-input-1").send_keys("598745")

        # Add click on the "Log in"
        driver.find_element_by_css_selector(".ion-color").click()

        time.sleep(5)

        # Add click on the "เพิ่มกิจกรรม"
        self.driver.find_element_by_css_selector(".ion-color-success").click()

        time.sleep(2)
        # Add click on the "ปัจจัยการผลิด"
        self.driver.find_element_by_css_selector(".item:nth-child(1) > .sc-ion-label-md-h:nth-child(2) > h3").click()

        time.sleep(2)

        assert "No results found." not in driver.page_source


    def test_add(self):
        driver = self.driver

        # Start and open browser
        driver.get("https://top-upstream-client.mulberrysoft.com/")
        self.assertIn("Thai Organic Platform", driver.title)

        # Log-in by username
        driver.find_element_by_name("ion-input-0").send_keys("demo004")

        # Log-in by password
        driver.find_element_by_name("ion-input-1").send_keys("598745")

        # Add click on the "Log in"
        driver.find_element_by_css_selector(".ion-color").click()

        time.sleep(5)

        # Go to the "หน้าเมนูบุคคล"
        self.driver.find_element_by_css_selector("#tab-button-menu > .md:nth-child(1)").click()

        time.sleep(2)

        # Add click on the "ข้อมูลส่วนตัว"
        self.driver.find_element_by_css_selector(".md:nth-child(1) > .item:nth-child(1) h3").click()

        time.sleep(5)

        # Change Email Address
        # driver.find_element_by_css_selector(".ion-activated").click()
        # driver.find_element_by_css_selector(".ion-activated > .alert-button-inner").click()
        # select = Select(driver.find_element_by_css_selector(".ion-activated > .ng-untouched"))
        # select.select_by_visible_text('พาน')
        # driver.find_elements_by_css_selector(".ion-activated > .alert-button-inner")

        assert "No results found." not in driver.page_source



    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()

