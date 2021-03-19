from POM_mainversion.locators import *

class SellingPage():

    def __init__(self, driver):

        self.driver = driver

        self.plant_interface = Locator.interface_button
        self.into_selling = Locator.click_selling
        self.select_selling_image = Locator.selling_selection
        self.selling_next = Locator.next_tab_function
        self.selling_value = Locator.selling_value
        self.selling_price = Locator.selling_price
        self.selling_submit_confirm = Locator.selling_submit_confirm
        self.selling_marget = Locator.selling_marget
        self.selling_unit = Locator.selling_unit
        self.selling_unit_select = Locator.selling_unit_select
        self.selling_paid = Locator.selling_paid
        self.selling_menu = Locator.plant_menu
        self.selling_price = Locator.plant_price
        self.selling_submit = Locator.selling_submit


    def into_sellingPage(self):
        self.driver.find_element_by_xpath(self.into_selling).click()
        self.driver.find_element_by_xpath(self.select_selling_image).click()
        self.driver.find_element_by_xpath(self.selling_next).click()

    def select_marget_picture(self):
        self.driver.find_element_by_xpath(self.selling_marget).click()
        self.driver.find_element_by_xpath(self.selling_next).click()

    def select_unit_selling(self):
        self.driver.find_element_by_xpath(self.selling_unit).click()
        self.driver.find_element_by_xpath(self.selling_unit_select).click()
        self.driver.find_element_by_xpath(self.selling_submit_confirm).click()

    def selling_enter_paid(self, paid):
        self.driver.find_element_by_xpath(self.selling_paid).clear()
        self.driver.find_element_by_xpath(self.selling_paid).send_keys(paid)

    def selling_enter_value(self, value):
        self.driver.find_element_by_xpath(self.selling_value).clear()
        self.driver.find_element_by_xpath(self.selling_value).send_keys(value)

    def selling_enter_price(self, price):
        self.driver.find_element_by_xpath(self.selling_price).clear()
        self.driver.find_element_by_xpath(self.selling_price).send_keys(price)
        self.driver.find_element_by_xpath(self.selling_next).click()

    def selling_enter_menu(self, menu):
        self.driver.find_element_by_xpath(self.selling_menu).clear()
        self.driver.find_element_by_xpath(self.selling_menu).send_keys(menu)

    def selling_enter_prices(self, prices):
        self.driver.find_element_by_xpath(self.selling_price).clear()
        self.driver.find_element_by_xpath(self.selling_price).send_keys(prices)
        self.driver.find_element_by_xpath(self.selling_next).click()

    def selling_confirm_submit(self):
        self.driver.find_element_by_xpath(self.selling_submit).click()
        self.driver.find_element_by_xpath(self.selling_submit_confirm).click()





