from POM_test.locators import *

class PlantPage():

    def __init__(self, driver):

        self.driver = driver

        self.into_plant = Locator.click_plant
        self.upload_plant_image = Locator.confirm_profile_planting
        self.plant_next_confirm = Locator.next_confirm
        self.plant_selector = Locator.plant_crops_selector
        self.plant_crop = Locator.add_plant_crops
        self.plant_amount = Locator.add_plant_amount
        self.plant_products = Locator.plant_products
        self.plant_unit = Locator.plant_garden_unit
        self.plant_unit_selector = Locator.garden_selection_unit
        self.plant_area = Locator.add_plant_area
        self.plant_area_unit = Locator.plant_area_unit
        self.plant_area_unit_selector = Locator.plant_area_unit_selector
        self.plant_paid = Locator.plant_paid
        self.plant_confirm = Locator.plant_confirm
        self.plant_garden = Locator.plant_garden
        self.plant_garden_selector = Locator.plant_garden_selector
        self.plant_products_unit = Locator.plant_products_unit
        self.plant_products_selector = Locator.plant_products_selector
        self.plant_submit = Locator.plant_submit
        self.plant_submit_confirm = Locator.plant_confirm_submit


    def into_plantPage(self):
        self.driver.find_element_by_css_selector(self.into_plant).click()

    def upload_picture(self):
        self.driver.find_element_by_id(self.upload_plant_image).send_keys("C:/Users/voraw/Desktop/Picture/work/fr5.jpg")

    def next_function(self):
        self.driver.find_element_by_xpath(self.plant_next_confirm).click()

    def plant_enter_crops(self):
        self.driver.find_element_by_xpath(self.plant_crop).click()
        self.driver.find_element_by_xpath(self.plant_selector).click()
        self.driver.find_element_by_xpath(self.plant_confirm).click()

    def plant_enter_garden(self):
        self.driver.find_element_by_xpath(self.plant_garden).click()
        self.driver.find_element_by_xpath(self.plant_garden_selector).click()
        self.driver.find_element_by_xpath(self.plant_confirm).click()

    def plant_enter_area_unit(self):
        self.driver.find_element_by_xpath(self.plant_area_unit).click()
        self.driver.find_element_by_xpath(self.plant_area_unit_selector).click()
        self.driver.find_element_by_xpath(self.plant_confirm).click()

    def plant_enter_area(self, area):
        self.driver.find_element_by_xpath(self.plant_area).clear()
        self.driver.find_element_by_xpath(self.plant_area).send_keys(area)

    def plant_enter_products(self, products):
        self.driver.find_element_by_xpath(self.plant_products).clear()
        self.driver.find_element_by_xpath(self.plant_products).send_keys(products)

    def plant_enter_value(self, value):
        self.driver.find_element_by_xpath(self.plant_amount).clear()
        self.driver.find_element_by_xpath(self.plant_amount).send_keys(value)

    def plant_enter_unit(self):
        self.driver.find_element_by_xpath(self.plant_unit).click()
        self.driver.find_element_by_xpath(self.plant_unit_selector).click()
        self.driver.find_element_by_xpath(self.plant_confirm).click()

    def plant_enter_unit_products(self):
        self.driver.find_element_by_xpath(self.plant_products_unit).click()
        self.driver.find_element_by_xpath(self.plant_products_selector).click()
        self.driver.find_element_by_xpath(self.plant_confirm).click()

    def plant_enter_paid(self, paid):
        self.driver.find_element_by_xpath(self.plant_paid).clear()
        self.driver.find_element_by_xpath(self.plant_paid).send_keys(paid)

    def plant_enter_submit(self):
        self.driver.find_element_by_xpath(self.plant_submit).click()
        self.driver.find_element_by_xpath(self.plant_submit_confirm).click()



