from POM_mainversion.locators import *

class HarvestPage():

    def __init__(self, driver):

        self.driver = driver

        self.plant_interface = Locator.interface_button
        self.upload_image = Locator.upload_image_object
        self.into_harvest = Locator.click_harvest
        self.harvest_plant_image = Locator.predict_planting
        self.harvest_next = Locator.predict_next
        self.harvest_device = Locator.harvest_device
        self.harvest_menu = Locator.plant_menu
        self.harvest_price = Locator.plant_price
        self.harvest_confirm = Locator.predict_submit_confirm
        self.harvest_value = Locator.harvest_value
        self.harvest_unit = Locator.harvest_unit
        self.harvest_unit_selection = Locator.harvest_unit_selection
        self.harvest_accept = Locator.harvest_select_accept
        self.harvest_submit = Locator.plant_submit
        self.harvest_next_confirm = Locator.plant_next_confirm
        self.harvest_delete = Locator.harvest_delete
        self.harvest_keep = Locator.harvest_keep
        self.harvest_next_confirm = Locator.plant_next_confirm

    def into_harvestPage(self):
        self.driver.find_element_by_xpath(self.into_harvest).click()
        self.driver.find_element_by_xpath(self.harvest_plant_image).click()
        self.driver.find_element_by_xpath(self.harvest_next).click()

    def select_device(self):
        self.driver.find_element_by_xpath(self.harvest_device).click()
        self.driver.find_element_by_xpath(self.harvest_next).click()

    def upload_picture_predict(self):
        self.driver.find_element_by_id(self.upload_image).send_keys("C:/Users/voraw/Desktop/Picture/work/fr5.jpg")

    def harvest_enter_menu(self, menu):
        self.driver.find_element_by_xpath(self.harvest_menu).clear()
        self.driver.find_element_by_xpath(self.harvest_menu).send_keys(menu)

    def harvest_enter_price(self, price):
        self.driver.find_element_by_xpath(self.harvest_price).clear()
        self.driver.find_element_by_xpath(self.harvest_price).send_keys(price)
        self.driver.find_element_by_xpath(self.harvest_next).click()

    def harvest_enter_value(self, value):
        self.driver.find_element_by_xpath(self.harvest_value).clear()
        self.driver.find_element_by_xpath(self.harvest_value).send_keys(value)

    def harvest_selection(self):
        self.driver.find_element_by_xpath(self.harvest_unit).click()
        self.driver.find_element_by_xpath(self.harvest_unit_selection).click()
        self.driver.find_element_by_xpath(self.harvest_accept).click()

    def harvest_delete_input(self, delete):
        self.driver.find_element_by_xpath(self.harvest_delete).clear()
        self.driver.find_element_by_xpath(self.harvest_delete).send_keys(delete)

    def harvest_keep_input(self, keep):
        self.driver.find_element_by_xpath(self.harvest_keep).clear()
        self.driver.find_element_by_xpath(self.harvest_keep).send_keys(keep)
        self.driver.find_element_by_xpath(self.harvest_next).click()

    def harvest_confirm_submit(self):
        self.driver.find_element_by_xpath(self.harvest_submit).click()
        self.driver.find_element_by_xpath(self.harvest_next_confirm).click()







