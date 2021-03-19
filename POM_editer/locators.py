class Locator():

    # Login page objects
    username_textbox_name = "ion-input-0"
    password_textbox_name = "ion-input-1"
    login_button_tag_name = "ion-button"

    # home page objects
    welcome_id = "tab-button-menu"
    edit_profile_xpath = "//h3[contains(.,'ข้อมูลส่วนตัว')]"
    logout_xpath = "//h3[contains(.,'ออกจากระบบ')]"

    #edit page objects
    upload_image = "/html/body/app-root/ion-app/ion-router-outlet/app-farmer/ion-tabs/div/ion-router-outlet/app-profile/ion-content/section[1]/app-upload-image/ion-button"
    edit_address_name = "ion-input-1"
    edit_first_name_name = "ion-input-2"
    edit_email_name = "ion-input-3"
    edit_phone_number_name = "ion-input-4"