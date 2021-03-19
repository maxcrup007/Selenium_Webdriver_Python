from POM_test.locators import *

class HarvestPage():

    def __init__(self, driver):

        self.driver = driver

        self.into_harvest = Locator.click_harvest
        self.upload_harvest_image = Locator.upload_harvest_image
        self.next_function = Locator.harvest_next
        self.harvest_crops = Locator.harvest_crops
        self.harvest_select = Locator.harvest_selection
        self.harvest_accept = Locator.harvest_accept
        self.harvest_value = Locator.harvest_value
        self.harvest_unit = Locator.harvest_unit
        self.harvest_unit_select = Locator.harvest_unit_selection
        self.harvest_confirm = Locator.harvest_select_accept
        self.harvest_paid = Locator.harvest_paid
        self.harvest_submit = Locator.harvest_submit

    def into_predictPage(self):
        self.driver.find_element_by_css_selector(self.into_harvest).click()

    def upload_image(self):
        self.driver.find_element_by_id(self.upload_harvest_image).send_keys("C:/Users/voraw/Desktop/Picture/work/pre-8.jpg")
        self.driver.find_element_by_xpath(self.next_function).click()

    def harvest_crops_choose(self):
        self.driver.find_element_by_xpath(self.harvest_crops).click()
        self.driver.find_element_by_xpath(self.harvest_select).click()
        self.driver.find_element_by_xpath(self.harvest_accept).click()

    def harvest_value_crops(self, value):
        self.driver.find_element_by_xpath(self.harvest_value).clear()
        self.driver.find_element_by_xpath(self.harvest_value).send_keys(value)

    def harvest_unit_choose(self):
        self.driver.find_element_by_xpath(self.harvest_unit).click()
        self.driver.find_element_by_xpath(self.harvest_unit_select).click()
        self.driver.find_element_by_xpath(self.harvest_confirm).click()

    def harvest_paid_crops(self, paid):
        self.driver.find_element_by_xpath(self.harvest_paid).clear()
        self.driver.find_element_by_xpath(self.harvest_paid).send_keys(paid)

    def harvest_submit_totally(self):
        self.driver.find_element_by_xpath(self.harvest_submit).click()
        self.driver.find_element_by_xpath(self.harvest_confirm).click()
