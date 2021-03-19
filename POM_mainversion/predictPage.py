from POM_mainversion.locators import *

class PredictPage():

    def __init__(self, driver):

        self.driver = driver

        self.plant_interface = Locator.interface_button
        self.upload_image = Locator.upload_image_object
        self.into_predict = Locator.click_predict
        self.predict_plant_image = Locator.predict_planting
        self.predict_next = Locator.predict_next
        self.predict_marget = Locator.predict_marget
        self.predict_unit = Locator.predict_unit
        self.predict_unit_selected = Locator.predict_unit_selection
        self.predict_confirm = Locator.predict_submit_confirm
        self.predict_value = Locator.predict_value
        self.predict_submit = Locator.plant_submit
        self.predict_next_confirm = Locator.plant_next_confirm




    def into_predictPage(self):
        self.driver.find_element_by_xpath(self.into_predict).click()
        self.driver.find_element_by_xpath(self.predict_plant_image).click()
        self.driver.find_element_by_xpath(self.predict_next).click()

    def select_marget(self):
        self.driver.find_element_by_xpath(self.predict_marget).click()
        self.driver.find_element_by_xpath(self.predict_next).click()

    def upload_picture_predict(self):
        self.driver.find_element_by_id(self.upload_image).send_keys("C:/Users/voraw/Desktop/Picture/work/fr5.jpg")

    def select_predict_unit(self):
        self.driver.find_element_by_xpath(self.predict_unit).click()
        self.driver.find_element_by_xpath(self.predict_unit_selected).click()
        self.driver.find_element_by_xpath(self.predict_confirm).click()

    def predict_enter_value(self, value):
        self.driver.find_element_by_xpath(self.predict_value).clear()
        self.driver.find_element_by_xpath(self.predict_value).send_keys(value)
        self.driver.find_element_by_xpath(self.predict_next).click()

    def predict_confirm_submit(self):
        self.driver.find_element_by_xpath(self.predict_submit).click()
        self.driver.find_element_by_xpath(self.predict_next_confirm).click()





