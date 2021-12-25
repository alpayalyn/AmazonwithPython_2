import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver


import unittest # Its taken from Java JUnit. It tells to 
from selenium import webdriver

class AmazonHomePage(unittest.TestCase):
    base_URL="https://www.amazon.com"

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  #10 is in seconds

    def test_load_home_page(self):
        self.driver.get(self.base_URL)
        self.assertIn("Amazon",self.driver.title) # It might be a problem. ??

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()