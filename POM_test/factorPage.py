from POM_test.locators import *
import os

class FactorPage():

    def __init__(self, driver):
        self.driver = driver

        self.into_factor = Locator.click_factor  # xpath = //ion-tab-button[@id='tab-button-menu']/ion-icon
        self.edit_profile_xpath = Locator.factor_next_confirm
        self.confirm_profile = Locator.confirm_profile_factor
        self.factor_next_confirm = Locator.factor_next_confirm
        self.add_unit = Locator.add_factor_unit
        self.unit_selection = Locator.add_factor_unit_selection
        self.unit_confirm = Locator.add_factor_unit_confirm
        self.add_category = Locator.add_factor_category
        self.category_selection = Locator.add_factor_category_selection
        self.category_confirm = Locator.add_factor_category_confirm
        self.add_name = Locator.add_factor_name
        self.add_value = Locator.add_factor_value
        self.add_price = Locator.add_factor_price
        self.factor_enter_complete = Locator.add_factor_complete
        self.factor_enter_confirm_complete = Locator.add_factor_confirm_complete

    def into_factorPage(self):
        self.driver.find_element_by_css_selector(self.into_factor).click()

    def upload_picture(self):
        self.driver.find_element_by_id(self.confirm_profile).send_keys("C:/Users/voraw/Desktop/Picture/work/fr5.jpg")

    def next_function(self):
        self.driver.find_element_by_xpath(self.factor_next_confirm).click()

    def factor_enter_category(self):
        self.driver.find_element_by_xpath(self.add_category).click()
        self.driver.find_element_by_xpath(self.category_selection).click()
        self.driver.find_element_by_xpath(self.category_confirm).click()

    def factor_enter_name(self, name):
        self.driver.find_element_by_name(self.add_name).clear()
        self.driver.find_element_by_name(self.add_name).send_keys(name)

    def factor_enter_value(self, value):
        self.driver.find_element_by_name(self.add_value).clear()
        self.driver.find_element_by_name(self.add_value).send_keys(value)

    def factor_enter_unit(self):
        self.driver.find_element_by_xpath(self.add_unit).click()
        self.driver.find_element_by_xpath(self.unit_selection).click()
        self.driver.find_element_by_xpath(self.unit_confirm).click()

    def factor_enter_price(self, price):
        self.driver.find_element_by_name(self.add_price).clear()
        self.driver.find_element_by_name(self.add_price).send_keys(price)

    def factor_enter_confirm(self):
        self.driver.find_element_by_xpath(self.factor_enter_complete).click()

    def factor_confirm(self):
        self.driver.find_element_by_xpath(self.factor_enter_confirm_complete).click()

