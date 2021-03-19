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
