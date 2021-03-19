class Locator():

    # Login page objects
    username_textbox_name = "ion-input-0"
    password_textbox_name = "ion-input-1"
    login_button_tag_name = "ion-button"

    # home page objects
    welcome_id = "tab-button-menu"
    edit_profile_xpath = "//h3[contains(.,'ข้อมูลส่วนตัว')]"
    logout_xpath = "//h3[contains(.,'ออกจากระบบ')]"

    # edit page objects
    upload_image = "/html/body/app-root/ion-app/ion-router-outlet/app-farmer/ion-tabs/div/ion-router-outlet/app-profile/ion-content/section[1]/app-upload-image/ion-button"
    edit_address_name = "ion-input-1"
    edit_first_name_name = "ion-input-2"
    edit_email_name = "ion-input-3"
    edit_phone_number_name = "ion-input-4"
    next_confirm = "//ion-col[2]/ion-button"
    go_main_menu = "//ion-icon[@name='menu-outline']"
    edit_garden_detail = "//ion-item[2]/ion-label/h3"
    edit_seed_detail = ""

    # Add Interface
    click_factor = ".stock"
    click_plant = ".planting"
    click_caring = ".manage"
    click_predict = ".predict"
    click_harvest = ".harvest"
    click_selling = ".selling"

    # Data Garden
    detail_garden = "//ion-segment-button[@value='garden']"
    tab_detail_garden = "//ion-button"
    upload_garden_image = "imageUpload1"
    name_garden = "html/body/app-root/ion-app/ion-model/div/app-modal-garden/ion-content/section[2]/form/ion-list/ion-item[1]/ion-input/input"
    number_garden = "html/body/app-root/ion-app/ion-model/div/app-modal-garden/ion-content/section[2]/form/ion-list/ion-item[2]/ion-input/input"
    area_garden = "html/body/app-root/ion-app/ion-model/div/app-modal-garden/ion-content/section[2]/form/ion-list/div[1]/ion-item/ion-input/input"
    garden_selection_unit = "//button[3]/div/div[2]"
    garden_input_unit = "//ion-select"
    garden_input_accept = "//button[2]/span"
    garden_owner = "//div/app-modal-garden/ion-content/section[2]/form/ion-list/ion-item[3]/ion-select"
    garden_owner_selection = "//button/div/div[2]"
    garden_in_district = "//div/app-modal-garden/ion-content/section[2]/form/ion-list/ion-item[7]/ion-select"
    garden_status = "//div/app-modal-garden/ion-content/section[2]/form/ion-list/ion-item[9]/ion-select"
    garden_status_selection = "//button[4]/div/div[2]"
    garden_submit_form = "//form/ion-button"
    garden_submit_confirm = "//button[2]/span"

    # Data Crops
    detail_crops = "//ion-item[3]/ion-label/h3"
    crops_select = "//ion-button"
    crops_category = "//div/app-modal-product/ion-content/section/form/ion-list/ion-item/ion-select"
    crops_select_category = "//button[3]/div/div[2]"
    crops_accept = "//button[2]/span"
    crops_planting = "//div/app-modal-product/ion-content/section/form/ion-list/ion-item[2]/ionic-selectable/div/button"
    crops_select_planting = "//ion-item-group/ion-item[2]/ion-label"
    crops_standard = "//div/app-modal-product/ion-content/section/form/ion-list/ion-item[3]/ion-select"
    crops_select_standard = "//button[5]/div/div[2]"
    crops_submit = ".ion-activated"
    crops_submit_confirm = "//button[2]/span"

    quiet_peace = ""

    # Factor Page
    edit_profile_factor = ".ion-activated"
    confirm_profile_factor = "imageUpload1"
    factor_next_confirm = "//ion-col[2]/ion-button"
    choose_category_factor = "//button[@id='alert-input-3-3']/div/div[2]"
    add_factor_name = "ion-input-2"
    add_factor_value = "ion-input-3"
    add_factor_price = "ion-input-4"
    add_factor_category = "//ion-select"
    add_factor_category_selection = "//button[3]/div/div[2]"
    add_factor_category_confirm = "//button[2]/span"
    add_factor_unit = "//ion-item[2]/ion-select"
    add_factor_unit_selection = "//button[4]/div/div[2]"
    add_factor_unit_confirm = "//button[2]/span"
    add_factor_complete = "//ion-col[2]/ion-button"
    add_factor_confirm_complete = "//button[2]/span"

    # Plant Page

    confirm_profile_planting = "imageUpload1"
    plant_next_confirm = "//ion-col[2]/ion-button"
    add_plant_amount = "//ion-input/input"
    add_plant_area = "//ion-list[4]/ion-item/ion-input/input"
    add_plant_category = "//ion-select"
    add_plant_crops = "//ion-select"
    plant_crops_selector = "//button[5]/div/div[2]"
    plant_confirm = "//button[2]/span"
    plant_garden = "//ion-list[2]/ion-item/ion-select"
    plant_garden_selector = "//button/div/div[2]"
    plant_garden_unit = "//ion-item[2]/ion-select"
    plant_unit_selector = "//button[5]/div/div[2]"
    plant_area_unit = "//ion-list[4]/ion-item[2]/ion-select"
    plant_area_unit_selector = "//button[3]/div/div[2]"
    plant_products = "//ion-list[5]/ion-item/ion-input/input"
    plant_products_unit = "//ion-list[5]/ion-item[2]/ion-select"
    plant_products_selector = "//button[5]/div/div[2]"
    plant_paid = "//ion-list[6]/ion-item/ion-input/input"
    plant_submit = "//ion-col[2]/ion-button"
    plant_confirm_submit = "//button[2]/span"

    # Care Page
    upload_care_image = "imageUpload1"
    next_tab_function = "//ion-col[2]/ion-button"
    care_choose_plant = "//ion-button"
    care_selection = "//div/app-modal-checkbox-product/ion-content/ion-card/ion-grid/ion-row/ion-col[2]"
    care_confirm_select = "//ion-buttons[2]/ion-button"
    care_paid = "//input"
    care_submit = "//ion-col[2]/ion-button"
    care_submit_confirm = "//button[2]/span"

    # Predict Page
    upload_predict_image = "imageUpload1"
    predict_next = "//ion-col[2]/ion-button"
    predict_planting = "//ion-button"
    predict_selection = "//ion-content/ion-card/ion-grid/ion-row/ion-col[2]/ion-card-content/p"
    predict_confirm = "//ion-buttons[2]/ion-button"
    predict_marget = "//ion-select"
    predict_marget_select = "//button/div/div"
    predict_accept = "//button[2]/span"
    predict_value = "//ion-input/input"
    predict_unit = "//ion-item[2]/ion-select"
    predict_unit_selection = "//button[4]/div/div[2]"
    predict_submit = "//ion-col[2]/ion-button"
    predict_submit_confirm = "//button[2]/span"

    # Harvest Page
    upload_harvest_image = "imageUpload1"
    harvest_next = "//ion-col[2]/ion-button"
    harvest_crops = "//ion-button"
    harvest_selection = "//div/app-modal-checkbox-product/ion-content/ion-card/ion-grid/ion-row/ion-col/span"
    harvest_accept = "//ion-buttons[2]/ion-button"
    harvest_value = "//input"
    harvest_unit = "//ion-select"
    harvest_unit_selection = "//button[2]/div/div[2]"
    harvest_select_accept = "//button[2]/span"
    harvest_paid = "//ion-list[3]/ion-item/ion-input/input"
    harvest_submit = "//ion-col[2]/ion-button"

    # Selling Page
    selling_crops = "//ion-button"
    selling_crops_select = "//p[2]"
    selling_crops_confirm = "//ion-buttons[2]/ion-button"
    selling_marget = "//ion-select"
    selling_marget_select = "//button/div/div"
    selling_confirm = "//button[2]/span"
    selling_value = "//ion-input/input"
    selling_unit = "//ion-item[2]/ion-select"
    selling_unit_select = "//button[4]/div/div[2]"
    selling_price = "//ion-item[3]/ion-input/input"
    selling_submit = "//ion-col[2]/ion-button"
    selling_submit_confirm = "//button[2]/span"

    # scroll bar
    scroll_bar = "inner-scroll scroll-y"

    # Profile Page
    profile_page = "//h3"
    profile_upload_image = "//ion-button"
    profile_name = "//ion-input/input"
    profile_email = "//ion-item[2]/ion-input/input"
    profile_birthday = "//app-date-time/ion-button"
    profile_birthday_day = "//ion-col/ion-item/ion-select"
    profile_birthday_days = "//button[4]/div/div"
    profile_birthday_month = "//ion-col[2]/ion-item/ion-select"
    profile_birthday_months = "//button[5]/div/div[2]"
    profile_birthday_year = "//ion-col[3]/ion-item/ion-select"
    profile_birthday_years = "//button[99]/div/div[2]"
    profile_birthday_ok = "//button[2]/span"
    profile_birthday_accept = "//ion-buttons[2]/ion-button"
    profile_phone = "//ion-item[4]/ion-input/input"
    profile_dialog = ""
    profile_address = "//textarea"
    profile_submit = "//form/ion-button"
    profile_confirm = "//button[2]/span"














# /html/body/app-root/ion-app/ion-modal/div/app-modal-garden/ion-content/section[2]/form/ion-list/ion-item/ion-input/input

# /html/body/app-root/ion-app/ion-modal/div/app-modal-garden/ion-content/section[2]/form/ion-list/ion-item[@class='item md in-list ion-focusable hydrated item-label item-interactive item-input ion-pristine ion-invalid ion-touched']/ion-input[@class='ng-pristine ng-invalid sc-ion-input-md-h sc-ion-input-md-s md hydrated ng-touched ion-pristine ion-invalid ion-touched']/input[@class='native-input sc-ion-input-md']