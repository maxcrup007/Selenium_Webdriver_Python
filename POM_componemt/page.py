from POM_componemt.locators import *


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.first_name_textbox_name = Locator.first_name_textbox_name
        self.last_name_textbox_name = Locator.last_name_textbox_name
        self.phone_textbox_name = Locator.phone_textbox_name
        self.country_textbox_name = Locator.country_textbox_name
        self.city_textbox_name = Locator.city_textbox_name
        self.email_textbox_name = Locator.email_textbox_name
        self.upload_file_name = Locator.upload_file_name
        self.submit_button_name = "Submit"

    def enter_first_name(self, first_name):
        self.driver.find_element_by_name(self.first_name_textbox_name).clear()
        self.driver.find_element_by_name(self.first_name_textbox_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element_by_name(self.last_name_textbox_name).clear()
        self.driver.find_element_by_name(self.last_name_textbox_name).send_keys(last_name)

    def enter_phone(self, phone):
        self.driver.find_element_by_name(self.phone_textbox_name).clear()
        self.driver.find_element_by_name(self.phone_textbox_name).send_keys(phone)

    def enter_country(self, country):
        self.driver.find_element_by_name(self.country_textbox_name).clear()
        self.driver.find_element_by_name(self.country_textbox_name).send_keys(country)

    def enter_city(self, city):
        self.driver.find_element_by_name(self.city_textbox_name).clear()
        self.driver.find_element_by_name(self.city_textbox_name).send_keys(city)

    def enter_email(self, email):
        self.driver.find_element_by_name(self.email_textbox_name).clear()
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(email)

    def upload_file(self, path):
        self.driver.find_element_by_name(self.upload_file_name).clear()
        self.driver.find_element_by_name(self.upload_file_name).send_keys(path)

    def click_submit(self):
        self.driver.find_element_by_name(self.submit_button_name).click()
