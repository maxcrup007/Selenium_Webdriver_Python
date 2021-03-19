from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SelectCalendar(object):

    driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
    driver.maximize_window()
    driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
    driver.implicitly_wait(10)
    driver.find_element_by_id("datepicker").click()

    all_dates = driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']//a")

    for d in all_dates:
        date = d.text
        print(date)
        if date == '22':
            d.click()
            break

    driver.close()
    driver.quit()


class Select_Dropeddown(object):

    driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
    driver.maximize_window()
    driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
    driver.implicitly_wait(10)

