from POM_mainversion.locators import *

class PlantPage():

    def __init__(self, driver):

        self.driver = driver

        self.plant_interface = Locator.interface_button
        self.into_plant = Locator.click_plant
        self.select_plant_image = Locator.plant_select_image
        self.plant_next = Locator.plant_next
        self.plant_segment = Locator.plant_segment
        self.plant_selected = Locator.plant_selected
        self.plant_menu = Locator.plant_menu
        self.plant_price = Locator.plant_price
        self.plant_next_confirm = Locator.plant_next_confirm
        self.plant_category = Locator.plant_category
        self.plant_category_selected = Locator.plant_category_selected
        self.plant_seed = Locator.plant_seed
        self.plant_seed_selected = Locator.plant_seed_selected
        self.plant_submit = Locator.plant_submit


    def into_plantPage(self):
        self.driver.find_element_by_xpath(self.plant_interface).click()
        self.driver.find_element_by_xpath(self.into_plant).click()

    def select_picture(self):
        self.driver.find_element_by_xpath(self.select_plant_image).click()
        self.driver.find_element_by_xpath(self.plant_next).click()

    def plant_segment_input(self):
        self.driver.find_element_by_xpath(self.plant_segment).click()
        self.driver.find_element_by_xpath(self.plant_selected).click()
        self.driver.find_element_by_xpath(self.plant_next).click()

    def plant_enter_menu(self, menu):
        self.driver.find_element_by_xpath(self.plant_menu).clear()
        self.driver.find_element_by_xpath(self.plant_menu).send_keys(menu)

    def plant_enter_price(self, price):
        self.driver.find_element_by_xpath(self.plant_price).clear()
        self.driver.find_element_by_xpath(self.plant_price).send_keys(price)
        self.driver.find_element_by_xpath(self.plant_next).click()

    def plant_category_input(self):
        self.driver.find_element_by_xpath(self.plant_category).click()
        self.driver.find_element_by_xpath(self.plant_category_selected).click()
        self.driver.find_element_by_xpath(self.plant_next_confirm).click()

    def plant_seed_input(self):
        self.driver.find_element_by_xpath(self.plant_seed).click()
        self.driver.find_element_by_xpath(self.plant_seed_selected).click()
        self.driver.find_element_by_xpath(self.plant_next_confirm).click()

    def plant_confirm_submit(self):
        self.driver.find_element_by_xpath(self.plant_submit).click()
        self.driver.find_element_by_xpath(self.plant_next_confirm).click()



