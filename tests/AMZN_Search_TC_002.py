
# bnk
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AmazonSearch(unittest.TestCase):
    
    base_URL = "https://www.amazon.com"
    search_term="WD My Passport 4TB"

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  #10 is in seconds             

    def test_search_for_a_term(self):
        self.driver.get(self.base_URL) 
        searchTextBox=self.driver.find_element_by_id("Samsung")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)

        self.assertIn(self.search_term,self.driver.title)
        self.assertNotIn("No results found.",self.driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()