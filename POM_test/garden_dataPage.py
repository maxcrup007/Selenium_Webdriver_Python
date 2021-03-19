from POM_test.locators import *
import os

class GardenFiledPage():

    def __init__(self, driver):
        self.driver = driver

        self.go_to_main_menu = Locator.go_main_menu
        self.edit_garden = Locator.edit_garden_detail
        self.find_detail_garden = Locator.detail_garden
        self.upload_picture = Locator.upload_garden_image
        self.tab_detail_garden = Locator.tab_detail_garden
        self.name_garden = Locator.name_garden
        self.number_garden = Locator.number_garden
        self.area_garden = Locator.area_garden
        self.accept_unit = Locator.garden_input_accept
        self.garden_unit = Locator.garden_input_unit
        self.selection_unit = Locator.garden_selection_unit
        self.garden_owner = Locator.garden_owner
        self.garden_owner_selection = Locator.garden_owner_selection
        self.garden_district = Locator.garden_in_district
        self.garden_status = Locator.garden_status
        self.garden_status_selection = Locator.garden_status_selection
        self.garden_submit = Locator.garden_submit_form
        self.garden_submit_confirm = Locator.garden_submit_confirm

    def into_gardenDetail(self):
        self.driver.find_element_by_xpath(self.go_to_main_menu).click()
        self.driver.find_element_by_xpath(self.edit_garden).click()
        self.driver.find_element_by_xpath(self.find_detail_garden).click()
        self.driver.find_element_by_xpath(self.tab_detail_garden).click()

    def upload_image_garden(self):
        self.driver.find_element_by_id(self.upload_picture).send_keys("C:/Users/voraw/Desktop/Picture/work/images.jpg")

    def garden_enter_unit(self):
        self.driver.find_element_by_xpath(self.garden_unit).click()
        self.driver.find_element_by_xpath(self.selection_unit).click()
        self.driver.find_element_by_xpath(self.accept_unit).click()

    def name_garden(self):
        self.driver.find_element_by_xpath(self.name_garden).get_attribute("innerHTML")
        self.driver.find_element_by_xpath(self.name_garden).send_keys("name")

    def number_garden(self):
        self.driver.find_element_by_xpath(self.number_garden).get_attribute("innerHTML")
        self.driver.find_element_by_xpath(self.number_garden).send_keys("007")

    def area_garden(self):
        self.driver.find_element_by_xpath(self.area_garden).get_attribute("innerHTML")
        self.driver.find_element_by_xpath(self.area_garden).send_keys("4")

    def garden_enter_owner(self):
        self.driver.find_element_by_xpath(self.garden_owner).click()
        self.driver.find_element_by_xpath(self.garden_owner_selection).click()
        self.driver.find_element_by_xpath(self.accept_unit).click()

    def garden_enter_district(self):
        self.driver.find_element_by_xpath(self.garden_district).click()
        self.driver.find_element_by_xpath(self.accept_unit).click()

    def garden_enter_status(self):
        self.driver.find_element_by_xpath(self.garden_status).click()
        self.driver.find_element_by_xpath(self.garden_status_selection).click()
        self.driver.find_element_by_xpath(self.accept_unit).click()

    def garden_submit(self):
        self.driver.find_element_by_xpath(self.garden_submit).click()
        self.driver.find_element_by_xpath(self.garden_submit_confirm).click()















