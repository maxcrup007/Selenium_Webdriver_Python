from POM_test.locators import *



class SellingPage():

    def __init__(self, driver):

        self.driver = driver

        self.into_selling = Locator.click_selling
        self.selling_crops = Locator.selling_crops
        self.selling_crops_select = Locator.selling_crops_select
        self.selling_crops_confirm = Locator.selling_crops_confirm
        self.selling_marget = Locator.selling_marget
        self.selling_marget_select = Locator.selling_marget_select
        self.selling_confirm = Locator.selling_confirm
        self.selling_value = Locator.selling_value
        self.selling_unit = Locator.selling_unit
        self.selling_unit_select = Locator.selling_unit_select
        self.selling_price = Locator.selling_price
        self.selling_submit = Locator.selling_submit
        self.selling_submit_confirm = Locator.selling_submit_confirm

    def into_sellingPage(self):
        self.driver.find_element_by_css_selector(self.into_selling).click()

    def selling_crops_choose(self):
        self.driver.find_element_by_xpath(self.selling_crops).click()
        self.driver.find_element_by_xpath(self.selling_crops_select).click()
        self.driver.find_element_by_xpath(self.selling_crops_confirm).click()

    def selling_marget_choose(self):
        self.driver.find_element_by_xpath(self.selling_marget).click()
        self.driver.find_element_by_xpath(self.selling_marget_select).click()
        self.driver.find_element_by_xpath(self.selling_confirm).click()

    def selling_value_totally(self, value):
        self.driver.find_element_by_xpath(self.selling_value).clear()
        self.driver.find_element_by_xpath(self.selling_value).send_keys(value)

    def selling_unit_choose(self):
        self.driver.find_element_by_xpath(self.selling_unit).click()
        self.driver.find_element_by_xpath(self.selling_unit_select).click()
        self.driver.find_element_by_xpath(self.selling_confirm).click()

    def selling_price_total(self, price):
        self.driver.find_element_by_xpath(self.selling_price).clear()
        self.driver.find_element_by_xpath(self.selling_price).send_keys(price)

    def selling_submit_finally(self):
        self.driver.find_element_by_xpath(self.selling_submit).click()
        self.driver.find_element_by_xpath(self.selling_submit_confirm).click()

    # def check2(self, driver, slidebar, sliderknob, percent):
    #
    #     height = slidebar.size['height']
    #     width = slidebar.size['width']
    #
    #     move = ActionChains(driver)
    #     slidebar = driver.find_element_by_xpath("//div[@id='slider']/a")
    #
    #     self.driver.switch_to_default_content()



