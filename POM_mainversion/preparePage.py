from POM_mainversion.locators import *
import os

class PreparePage():

    def __init__(self, driver):
        self.driver = driver

        self.into_prepare = Locator.click_prepare
        self.edit_profile_xpath = Locator.factor_next_confirm
        self.upload_image = Locator.upload_image_object
        self.prepare_card_selected = Locator.prepare_card
        self.prepare_next = Locator.prepare_next
        self.prepare_selected = Locator.prepare_selected
        self.prepare_selected2 = Locator.prepare_selected2
        self.prepare_selected3 = Locator.prepare_selected3
        self.prepare_segment = Locator.prepare_segment
        self.prepare_menu = Locator.prepare_menu
        self.prepare_price = Locator.prepare_price
        self.prepare_confirm = Locator.prepare_confirm

    def into_preparePage(self):
        self.driver.find_element_by_xpath(self.into_prepare).click()
        self.driver.find_element_by_xpath(self.prepare_card_selected).click()
        self.driver.find_element_by_xpath(self.prepare_next).click()

    def choose_category_prepare(self):
        self.driver.find_element_by_xpath(self.prepare_selected).click()
        self.driver.find_element_by_xpath(self.prepare_selected2).click()
        self.driver.find_element_by_xpath(self.prepare_selected3).click()
        self.driver.find_element_by_xpath(self.prepare_next).click()

    def directory_prepare(self):
        self.driver.find_element_by_xpath(self.prepare_segment).click()
        self.driver.find_element_by_xpath(self.prepare_selected).click()
        self.driver.find_element_by_xpath(self.prepare_next).click()

    def prepare_enter_menu(self, menu):
        self.driver.find_element_by_xpath(self.prepare_menu).clear()
        self.driver.find_element_by_xpath(self.prepare_menu).send_keys(menu)

    def prepare_enter_price(self, price):
        self.driver.find_element_by_xpath(self.prepare_price).clear()
        self.driver.find_element_by_xpath(self.prepare_price).send_keys(price)
        self.driver.find_element_by_xpath(self.prepare_next).click()
        self.driver.find_element_by_xpath(self.prepare_confirm).click()

    def factor_enter_unit(self):
        self.driver.find_element_by_xpath(self.factor_unit).click()
        self.driver.find_element_by_xpath(self.factor_unit_selection).click()
        self.driver.find_element_by_xpath(self.factor_unit_confirm).click()



    def factor_submit_complete(self):
        self.driver.find_element_by_xpath(self.factor_submit).click()
        self.driver.find_element_by_xpath(self.factor_confirm).click()

