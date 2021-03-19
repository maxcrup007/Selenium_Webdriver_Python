from POM_test.locators import *



class PredictPage():

    def __init__(self, driver):

        self.driver = driver

        self.into_predict = Locator.click_predict
        self.upload_predict_image = Locator.upload_predict_image
        self.next_function = Locator.predict_next
        self.predict_planting = Locator.predict_planting
        self.predict_selection = Locator.predict_selection
        self.predict_confirm = Locator.predict_confirm
        self.predict_marget = Locator.predict_marget
        self.predict_marget_select = Locator.predict_marget_select
        self.predict_accept = Locator.predict_accept
        self.predict_value = Locator.predict_value
        self.predict_unit = Locator.predict_unit
        self.predict_unit_selection = Locator.predict_unit_selection
        self.predict_submit = Locator.predict_submit
        self.predict_submit_confirm = Locator.predict_submit_confirm

    def into_predictPage(self):
        self.driver.find_element_by_css_selector(self.into_predict).click()

    def upload_image(self):
        self.driver.find_element_by_id(self.upload_predict_image).send_keys("C:/Users/voraw/Desktop/Picture/work/pre-8.jpg")
        self.driver.find_element_by_xpath(self.next_function).click()

    def predict_plant(self):
        self.driver.find_element_by_xpath(self.predict_planting).click()
        self.driver.find_element_by_xpath(self.predict_selection).click()
        self.driver.find_element_by_xpath(self.predict_confirm).click()

    def predict_select(self):
        self.driver.find_element_by_xpath(self.predict_marget).click()
        self.driver.find_element_by_xpath(self.predict_marget_select).click()
        self.driver.find_element_by_xpath(self.predict_accept).click()

    def predict_value_selected(self, value):
        self.driver.find_element_by_xpath(self.predict_value).clear()
        self.driver.find_element_by_xpath(self.predict_value).send_keys(value)

    def predict_unit_selected(self):
        self.driver.find_element_by_xpath(self.predict_unit).click()
        self.driver.find_element_by_xpath(self.predict_unit_selection ).click()
        self.driver.find_element_by_xpath(self.predict_accept).click()

    def predict_submit_value(self):
        self.driver.find_element_by_xpath(self.predict_submit).click()
        self.driver.find_element_by_xpath(self.predict_submit_confirm).click()





