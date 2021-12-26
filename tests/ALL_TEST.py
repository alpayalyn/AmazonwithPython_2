import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ViewProductDetails(unittest.TestCase):
    search_term="Samsung"
    base_URL="https://www.amazon.com"

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()
    # --- Steps for AMZN_Search_TC_001 ---
    def test_1load_home_page(self):      
        print("User lands on the Home Page")
        driver=self.driver
        driver.get(self.base_URL)        
        self.assertIn("Amazon",driver.title)

    # --- Steps for AMZN_Search_TC_002 ---
    def test_2search_for_a_term(self):
        print("User searches for specific Text and navigates there.")
        self.driver.get(self.base_URL)         
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)
        self.assertIn(self.search_term,self.driver.title)
        self.assertNotIn("No results found.",self.driver.page_source)   
        
    # --- Steps for AMZN_Search_TC_003 ---
    def test_3add_item_to_wishlist(self):
        print("Adds item to wishlist")
        self.driver.get(self.base_URL)         
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)
        self.assertIn(self.search_term,self.driver.title)
        self.assertNotIn("No results found.",self.driver.page_source)   
        self.driver.get(self.base_URL)         
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_class_name("aok-relative")[1].click()
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_id("add-to-wishlist-button-submit").click()
        self.assertTrue(self.driver.find_element_by_id("WLHUC_viewlist").is_displayed())

    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()