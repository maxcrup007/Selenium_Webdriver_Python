from POM_test.locators import *

class CarePage():

    def __init__(self, driver):

        self.driver = driver

        self.into_care = Locator.click_caring
        self.upload_care_image = Locator.upload_care_image
        self.next_function = Locator.next_tab_function
        self.choose_plant = Locator.care_choose_plant
        self.care_selection = Locator.care_selection
        self.care_confirm = Locator.care_confirm_select
        self.care_paid = Locator.care_paid
        self.care_submit = Locator.care_submit
        self.care_submit_confirm = Locator.care_submit_confirm




    def into_caringPage(self):
        self.driver.find_element_by_css_selector(self.into_care).click()

    def upload_picture(self):
        self.driver.find_element_by_id(self.upload_care_image).send_keys("C:/Users/voraw/Desktop/Picture/work/fr5.jpg")
        self.driver.find_element_by_xpath(self.next_function).click()

    def care_choose_plant(self):
        self.driver.find_element_by_xpath(self.choose_plant).click()
        self.driver.find_element_by_xpath(self.care_selection).click()
        self.driver.find_element_by_xpath(self.care_confirm).click()

    def care_enter_paid(self, paid):
        self.driver.find_element_by_xpath(self.care_paid).clear()
        self.driver.find_element_by_xpath(self.care_paid).send_keys(paid)

    def submit_confirm_care(self):
        self.driver.find_element_by_xpath(self.care_submit).click()
        self.driver.find_element_by_xpath(self.care_submit_confirm).click()