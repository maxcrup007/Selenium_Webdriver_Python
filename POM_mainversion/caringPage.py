from POM_mainversion.locators import *

class CaringPage():

    def __init__(self, driver):

        self.driver = driver

        self.plant_interface = Locator.interface_button
        self.into_caring = Locator.click_caring
        self.select_plant_image = Locator.caring_select
        self.care_next = Locator.next_tab_function
        self.care_action_1 = Locator.care_choose_plant
        self.care_action_2 = Locator.care_choose_plant2
        self.care_action_3 = Locator.care_choose_plant3
        self.plant_segment = Locator.plant_segment
        self.plant_selected = Locator.plant_selected
        self.care_problem = Locator.care_problem
        self.care_menu = Locator.plant_menu
        self.care_price = Locator.plant_price
        self.care_next_confirm = Locator.plant_next_confirm


    def into_carePage(self):
        self.driver.find_element_by_xpath(self.into_caring).click()
        self.driver.find_element_by_xpath(self.select_plant_image).click()
        self.driver.find_element_by_xpath(self.care_next).click()

    def select_picture(self):
        self.driver.find_element_by_xpath(self.select_plant_image).click()
        self.driver.find_element_by_xpath(self.care_next).click()

    def select_action_picture(self):
        self.driver.find_element_by_xpath(self.care_action_1).click()
        self.driver.find_element_by_xpath(self.care_action_2).click()
        self.driver.find_element_by_xpath(self.care_action_3).click()
        self.driver.find_element_by_xpath(self.care_next).click()

    def plant_segment_input(self):
        self.driver.find_element_by_xpath(self.plant_segment).click()
        self.driver.find_element_by_xpath(self.plant_selected).click()
        self.driver.find_element_by_xpath(self.care_next).click()

    def select_problem(self):
        self.driver.find_element_by_xpath(self.care_problem).click()
        self.driver.find_element_by_xpath(self.care_next).click()

    def plant_enter_menu(self, menu):
        self.driver.find_element_by_xpath(self.care_menu).clear()
        self.driver.find_element_by_xpath(self.care_menu).send_keys(menu)

    def plant_enter_price(self, price):
        self.driver.find_element_by_xpath(self.care_price).clear()
        self.driver.find_element_by_xpath(self.care_price).send_keys(price)
        self.driver.find_element_by_xpath(self.care_next).click()
        self.driver.find_element_by_xpath(self.care_next_confirm).click()





