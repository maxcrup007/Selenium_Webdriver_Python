from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/voraw/Downloads/Compressed/webdriver/chromedriver/chromedriver")
        self.driver.get("https://www.python.org/")

    