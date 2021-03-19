from POM_mainversion.locators import *
import os

class PlaningPage():

    def __init__(self, driver):
        self.driver = driver

        self.into_planing = Locator.planing_bar
        self.edit_profile_xpath = Locator.factor_next_confirm
        self.upload_image = Locator.upload_image_object
        self.interface = Locator.interface_button
        self.planing_case = Locator.planing_per_year
        self.planing_button = Locator.planning_button
        self.planing_garden = Locator.planning_garden
        self.planing_garden_select = Locator.planning_garden_select
        self.planing_confirm = Locator.planning_confirm
        self.planing_crops = Locator.planning_crops
        self.planing_crops_select = Locator.planning_crops_select
        self.planing_area = Locator.planning_area
        self.planing_area_dd = Locator.planning_area_dd
        self.planing_area_select = Locator.planning_area_select
        self.planing_amount = Locator.planning_amount
        self.planing_amount_dd = Locator.planning_amount_dd
        self.planing_amount_select = Locator.planning_amount_select
        self.planing_value = Locator.planning_value
        self.planing_value_dd = Locator.planning_value_dd
        self.planing_value_select = Locator.planning_value_select
        self.planning_submit = Locator.planning_submit
        self.planning_saved = Locator.planning_saved

    def into_plan(self):
        self.driver.find_element_by_xpath(self.into_planing).click()
        self.driver.find_element_by_xpath(self.planing_case).click()

    def click_plan_button(self):
        self.driver.find_element_by_xpath(self.planing_button).click()

    def plan_garden_input(self):
        self.driver.find_element_by_xpath(self.planing_garden).click()
        self.driver.find_element_by_xpath(self.planing_garden_select).click()
        self.driver.find_element_by_xpath(self.planing_confirm).click()

    def plan_crops_input(self):
        self.driver.find_element_by_xpath(self.planing_crops).click()
        self.driver.find_element_by_xpath(self.planing_crops_select).click()
        self.driver.find_element_by_xpath(self.planing_confirm).click()

    def plan_enter_area(self, area):
        self.driver.find_element_by_xpath(self.planing_area).clear()
        self.driver.find_element_by_xpath(self.planing_area).send_keys(area)

    def plan_area_input(self):
        self.driver.find_element_by_xpath(self.planing_area_dd).click()
        self.driver.find_element_by_xpath(self.planing_area_select).click()
        self.driver.find_element_by_xpath(self.planing_confirm).click()

    def plan_enter_amount(self, amount):
        self.driver.find_element_by_xpath(self.planing_amount).clear()
        self.driver.find_element_by_xpath(self.planing_amount).send_keys(amount)

    def plan_amount_input(self):
        self.driver.find_element_by_xpath(self.planing_amount_dd).click()
        self.driver.find_element_by_xpath(self.planing_amount_select).click()
        self.driver.find_element_by_xpath(self.planing_confirm).click()

    def plan_enter_value(self, value):
        self.driver.find_element_by_xpath(self.planing_value).clear()
        self.driver.find_element_by_xpath(self.planing_value).send_keys(value)

    def plan_value_input(self):
        self.driver.find_element_by_xpath(self.planing_value_dd).click()
        self.driver.find_element_by_xpath(self.planing_value_select).click()
        self.driver.find_element_by_xpath(self.planing_confirm).click()

    def plan_submit_confirm(self):
        self.driver.find_element_by_xpath(self.planning_submit).click()
        self.driver.find_element_by_xpath(self.planing_confirm).click()

    def plan_saved_confirm(self):
        self.driver.find_element_by_xpath(self.planning_saved).click()
        self.driver.find_element_by_xpath(self.planing_confirm).click()

