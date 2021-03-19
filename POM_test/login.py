from POM_test.locators import *


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = Locator.username_textbox_name
        self.password_textbox_name = Locator.password_textbox_name
        self.login_button_tag_name     = "ion-button"

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_tag_name(self.login_button_tag_name).click()
