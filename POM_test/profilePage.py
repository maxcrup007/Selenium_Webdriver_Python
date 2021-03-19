from POM_test.locators import *
from selenium.webdriver import ActionChains
import os

class ProfilePage():

    def __init__(self, driver):
        self.driver = driver

        self.go_to_main_menu = Locator.go_main_menu
        self.edit_profile = Locator.profile_page
        self.upload_picture = Locator.profile_upload_image
        self.profile_name = Locator.profile_name
        self.profile_email = Locator.profile_email
        self.profile_birthday = Locator.profile_birthday
        self.profile_birthday_day = Locator.profile_birthday_day
        self.profile_birthday_days = Locator.profile_birthday_days
        self.profile_birthday_month = Locator.profile_birthday_month
        self.profile_birthday_months = Locator.profile_birthday_months
        self.profile_birthday_year = Locator.profile_birthday_year
        self.profile_birthday_years = Locator.profile_birthday_years
        self.profile_birthday_ok = Locator.profile_birthday_ok
        self.profile_birthday_accept = Locator.profile_birthday_accept

        self.profile_phone = Locator.profile_phone
        self.profile_address = Locator.profile_address
        self.profile_submit = Locator.profile_submit
        self.profile_confirm = Locator.profile_confirm

    def into_profilePage(self):
        self.driver.find_element_by_xpath(self.go_to_main_menu).click()
        self.driver.find_element_by_xpath(self.edit_profile).click()
        # send_keys("C:/Users/voraw/Desktop/Picture/work/doge.jpg")

    def upload_picture_profile(self):
        self.driver.find_element_by_xpath(self.upload_picture).send_keys("C:/Users/voraw/Desktop/Picture/work/fr5.jpg")

    def profile_name_input(self, name):
        self.driver.find_element_by_xpath(self.profile_name).clear()
        self.driver.find_element_by_xpath(self.profile_name).send_keys(name)

    def profile_email_input(self, email):
        self.driver.find_element_by_xpath(self.profile_email).clear()
        self.driver.find_element_by_xpath(self.profile_email).send_keys(email)

    def profile_select_birthday(self):
        driver = self.driver

        self.driver.find_element_by_xpath(self.profile_birthday).click()
        self.driver.find_element_by_xpath(self.profile_birthday_day).click()
        self.driver.find_element_by_xpath(self.profile_birthday_days).click()
        self.driver.find_element_by_xpath(self.profile_birthday_ok).click()
        self.driver.find_element_by_xpath(self.profile_birthday_month).click()
        self.driver.find_element_by_xpath(self.profile_birthday_months).click()
        self.driver.find_element_by_xpath(self.profile_birthday_ok).click()
        self.driver.find_element_by_xpath(self.profile_birthday_year).click()
        scroll = driver.find_element_by_xpath("//button[99]/div/div[2]")
        action = ActionChains(driver)
        action.move_to_element(scroll).perform()
        self.driver.find_element_by_xpath(self.profile_birthday_years).click()
        self.driver.find_element_by_xpath(self.profile_birthday_ok).click()

    def profile_phone_number(self, phone):
        self.driver.find_element_by_xpath(self.profile_phone).clear()
        self.driver.find_element_by_xpath(self.profile_phone).send_keys(phone)

    def profile_address_text(self, address):
        self.driver.find_element_by_xpath(self.profile_address).clear()
        self.driver.find_element_by_xpath(self.profile_address).send_keys(address)

    def profile_submit_confirm(self):
        self.driver.find_element_by_xpath(self.profile_submit).click()
        self.driver.find_element_by_xpath(self.profile_confirm).click()






