from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from POM_test.locators import *


class ScrollbarPage():

    def __init__(self, driver):
        self.driver = driver
        self.scroll_garden = Locator
        self.scroll_garden_2 = Locator
        self.scroll_garden_3 = Locator
        self.scroll_controller = Locator

    def selling_scrolling(self):
        driver = self.driver
        scroll = driver.find_element_by_xpath("//*[text()='ขายหมดแล้วหรือยัง']")
        action = ActionChains(driver)
        action.move_to_element(scroll).perform()
        # action object creation to scroll

    def profile_scrolling(self):
        driver = self.driver
        scroll = driver.find_element_by_xpath("//ion-item[14]/div")
        action = ActionChains(driver)
        action.move_to_element(scroll).perform()

    def profile_scrolling2(self):
        driver = self.driver
        scroll = driver.find_element_by_xpath("//form/ion-button")
        action = ActionChains(driver)
        action.move_to_element(scroll).perform()

    def scroll_controller(self):
        driver = self.driver

    def scrolling_scr(self):
        driver = self.driver
        scr = self.scroll_controller()
        action_sct = ActionChains(driver)

        action = ActionChains.move_by_offset(0, 5000).perform()

        if scr > action:
            ActionChains.release()

        elif scr == action_sct:
            ActionChains.release()

    def scrolling_garden_1(self):
        driver = self.driver
        scroll = driver.find_element_by_xpath("//ion-item[4]/ion-input/input")
        action = ActionChains(driver)
        action.move_to_element(scroll).perform()
        # action object creation to scroll round 1

    def scrolling_garden_2(self):
        driver = self.driver
        scroll2 = driver.find_element_by_xpath("//ion-item[10]/ion-select")
        action = ActionChains(driver)
        action.move_to_element(scroll2).perform()
        # action object creation to scroll round 2

    def scrolling_garden_3(self):
        driver = self.driver
        scroll3 = driver.find_element_by_xpath("//form/ion-button")
        action = ActionChains(driver)
        action.move_to_element(scroll3).perform()
        # action object creation to scroll round 3




