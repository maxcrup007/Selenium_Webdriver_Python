from POM_mainversion.locators import *
import os


class Detail_Crops_Page():

    def __init__(self, driver):
        self.driver = driver
        self.into_detail_page = Locator.into_detail_page
        self.into_detail_crops = Locator.into_detail_crops
        self.add_crops = Locator.add_crops
        self.crops_selection = Locator.crops_select
        self.crops_category = Locator.crops_category
        self.crops_select_category = Locator.crops_select_category
        self.crops_confirm = Locator.crops_accept
        self.crops_planting = Locator.crops_planting
        self.crops_select_planting = Locator.crops_select_planting
        self.crops_standard = Locator.crops_standard
        self.crops_select_standard = Locator.crops_select_standard
        self.crops_submit = Locator.crop_submit_version
        self.crops_submit_confirm = Locator.crops_submit_confirm

    def into_crops(self):
        self.driver.find_element_by_xpath(self.into_detail_page).click()
        self.driver.find_element_by_xpath(self.into_detail_crops).click()
        self.driver.find_element_by_xpath(self.add_crops).click()

    def choose_category(self):
        self.driver.find_element_by_xpath(self.crops_category).click()
        self.driver.find_element_by_xpath(self.crops_select_category).click()
        self.driver.find_element_by_xpath(self.crops_confirm).click()

    def choose_crops(self):
        self.driver.find_element_by_xpath(self.crops_planting).click()
        self.driver.find_element_by_xpath(self.crops_select_planting).click()

    def choose_standard(self):
        self.driver.find_element_by_xpath(self.crops_standard).click()
        self.driver.find_element_by_xpath(self.crops_select_standard).click()
        self.driver.find_element_by_xpath(self.crops_confirm).click()

    def click_submit_confirm(self):
        self.driver.find_element_by_xpath(self.crops_submit).click()
        self.driver.find_element_by_xpath(self.crops_submit_confirm).click()


class Detail_Garden_Page():

    def __init__(self, driver):
        self.driver = driver
        self.into_detail_page = Locator.into_detail_page
        self.into_detail_garden = Locator.into_detail_garden
        self.garden_form = Locator.garden_form
        self.add_garden = Locator.add_garden
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

    def into_garden(self):
        self.driver.find_element_by_xpath(self.into_detail_page).click()
        self.driver.find_element_by_xpath(self.into_detail_garden).click()
        self.driver.find_element_by_xpath(self.garden_form).click()
        self.driver.find_element_by_xpath(self.add_garden).click()

    def upload_image_garden(self):
        self.driver.find_element_by_id(self.upload_picture).send_keys("C:/Users/voraw/Desktop/Picture/work/images.jpg")

    def garden_enter_unit(self):
        self.driver.find_element_by_xpath(self.garden_unit).click()
        self.driver.find_element_by_xpath(self.selection_unit).click()
        self.driver.find_element_by_xpath(self.accept_unit).click()

    def name_garden_input(self, name):
        self.driver.find_element_by_xpath(self.name_garden).clear()
        self.driver.find_element_by_xpath(self.name_garden).send_keys(name)

    def number_garden_input(self, number):
        self.driver.find_element_by_xpath(self.number_garden).clear()
        self.driver.find_element_by_xpath(self.number_garden).send_keys(number)

    def area_garden_input(self, area):
        self.driver.find_element_by_xpath(self.area_garden).clear()
        self.driver.find_element_by_xpath(self.area_garden).send_keys(area)

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

    def garden_accept_submit(self):
        self.driver.find_element_by_xpath(self.garden_submit).click()
        self.driver.find_element_by_xpath(self.garden_submit_confirm).click()




