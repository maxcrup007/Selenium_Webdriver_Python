from POM_mainversion.locators import *
import os

class FactorPage():

    def __init__(self, driver):
        self.driver = driver

        self.into_factor = Locator.click_factor
        self.edit_profile_xpath = Locator.factor_next_confirm
        self.upload_image = Locator.upload_image_object
        self.interface = Locator.interface_button
        self.choose_category = Locator.choose_category_factor
        self.category_selection = Locator.add_factor_category_selection
        self.category_confirm = Locator.add_factor_category_confirm
        self.factor_name = Locator.add_factor_name
        self.factor_value = Locator.add_factor_value
        self.factor_unit = Locator.add_factor_unit
        self.factor_unit_selection = Locator.add_factor_unit_selection
        self.factor_unit_confirm = Locator.add_factor_unit_confirm
        self.factor_price = Locator.add_factor_price
        self.factor_submit = Locator.add_factor_submit
        self.factor_confirm = Locator.add_factor_confirm_submit

    def into_factorPage(self):
        self.driver.find_element_by_xpath(self.interface).click()
        self.driver.find_element_by_xpath(self.into_factor).click()

    def upload_picture_factor(self):
        self.driver.find_element_by_id(self.upload_image).send_keys("C:/Users/voraw/Desktop/Picture/work/fr5.jpg")

    def choose_category_factors(self):
        self.driver.find_element_by_xpath(self.choose_category).click()
        self.driver.find_element_by_xpath(self.category_selection).click()
        self.driver.find_element_by_xpath(self.category_confirm).click()

    def factor_enter_name(self, name):
        self.driver.find_element_by_xpath(self.factor_name).clear()
        self.driver.find_element_by_xpath(self.factor_name).send_keys(name)

    def factor_enter_value(self, value):
        self.driver.find_element_by_xpath(self.factor_value).clear()
        self.driver.find_element_by_xpath(self.factor_value).send_keys(value)

    def factor_choose_value(self):
        self.driver.find_element_by_xpath()

    def factor_enter_unit(self):
        self.driver.find_element_by_xpath(self.factor_unit).click()
        self.driver.find_element_by_xpath(self.factor_unit_selection).click()
        self.driver.find_element_by_xpath(self.factor_unit_confirm).click()

    def factor_enter_price(self, price):
        self.driver.find_element_by_xpath(self.factor_price).clear()
        self.driver.find_element_by_xpath(self.factor_price).send_keys(price)

    def factor_submit_complete(self):
        self.driver.find_element_by_xpath(self.factor_submit).click()
        self.driver.find_element_by_xpath(self.factor_confirm).click()

