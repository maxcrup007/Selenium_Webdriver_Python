from POM_editer.locators import *
import os


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_id = "tab-button-menu" # xpath = //ion-tab-button[@id='tab-button-menu']/ion-icon
        self.edit_profile_xpath = "//h3[contains(.,'ข้อมูลส่วนตัว')]"
        self.logout_xpath = "//h3[contains(.,'ออกจากระบบ')]"
        self.upload_image = "/html/body/app-root/ion-app/ion-router-outlet/app-farmer/ion-tabs/div/ion-router-outlet/app-profile/ion-content/section[1]/app-upload-image/ion-button" # tag_name = "//ion-button[contains(.,'อัพโหลดรูป')]"

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_id).click()

    def click_editprofile(self):
        self.driver.find_element_by_xpath(self.edit_profile_xpath).click()

    def upload_image_profile(self):
        self.driver.find_element_by_xpath(self.upload_image).click()
        self.driver.find_element_by_xpath(self.upload_image).send_keys(os.getcwd() + "..Desktop/Picture/images.jpg")

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()

class EditProfile():

    def __init__(self, driver):
        self.driver = driver
        self.edit_address_name = Locator.edit_address_name
        self.edit_first_name_name = Locator.edit_first_name_name
        self.edit_email_name = Locator.edit_email_name
        self.edit_phone_number_name = Locator.edit_phone_number_name


    def enter_first_name(self, first_name):
        self.driver.find_element_by_name(self.edit_first_name_name).clear()
        self.driver.find_element_by_name(self.edit_first_name_name).send_keys(first_name)

    def enter_email(self, email):
        self.driver.find_element_by_name(self.edit_email_name).clear()
        self.driver.find_element_by_name(self.edit_email_name).send_keys(email)

    def enter_phone_number(self, phone_number):
        self.driver.find_element_by_name(self.edit_email_name).clear()
        self.driver.find_element_by_name(self.edit_email_name).send_keys(phone_number)

    def enter_address(self, address):
        self.driver.find_element_by_name(self.edit_email_name).clear()
        self.driver.find_element_by_name(self.edit_email_name).send_keys(address)