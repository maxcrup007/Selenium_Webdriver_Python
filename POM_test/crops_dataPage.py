from POM_test.locators import *
import os

class CropsPage():

    def __init__(self, driver):
        self.driver = driver

        self.go_to_main_menu = Locator.go_main_menu
        self.edit_crops = Locator.detail_crops
        self.crops_selection = Locator.crops_select
        self.crops_category = Locator.crops_category
        self.crops_select_category = Locator.crops_select_category
        self.crops_confirm = Locator.crops_accept
        self.crops_planting = Locator.crops_planting
        self.crops_select_planting = Locator.crops_select_planting
        self.crops_standard = Locator.crops_standard
        self.crops_select_standard = Locator.crops_select_standard
        self.crops_submit = Locator.crops_submit
        self.crops_submit_confirm = Locator.crops_submit_confirm

    def into_cropsDetail(self):
        self.driver.find_element_by_xpath(self.go_to_main_menu).click()
        self.driver.find_element_by_xpath(self.edit_crops).click()
        self.driver.find_element_by_xpath(self.crops_selection).click()

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

    def crops_submit(self):
        self.driver.find_element_by_css_selector(self.crops_submit).click()
        self.driver.find_element_by_xpath(self.crops_submit_confirm).click()


