import time
import page
import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):


    def setUp(self):
        print("Begin")
        self.driver = webdriver.Chrome("C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
        self.driver.get("https://www.python.org/")

    def test_title(self):
        Selenium_pythonPage = page.MainPage
        assert Selenium_pythonPage.is_title_matches()

    def test_search_python(self):
        mainPage = page.MainPage()
        assert  mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        search_result = page.SearchResultsPage(self.driver)
        assert search_result.is_results_found()

    def test_example(self):
        print("Test")
        assert True

    def test_example2(self):
        print("Test is Passed")
        assert False


    def not_test(self):
        print("this won't print")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
