from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Select(object):

    def __init__(self, web_element):
        if web_element.tag_name.lower() != "select":
            raise UnexpectedTagNameException(

            )