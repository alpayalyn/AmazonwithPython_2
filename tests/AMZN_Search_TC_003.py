# bnk
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AddItemToCart(unittest.TestCase):
    base_URL = "https://www.amazon.com"
    search_term = "Samsung"

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # 10 is in seconds

    def test_add_item_to_cart(self):
        self.driver.get(self.base_URL)
        searchTextBox = self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)
        self.driver.find_element_by_class_name("aok-relative")[0].click()
        self.driver.find_element_by_id("add-to-wishlist-button-submit").click()
 
    def tearDown(self):
        # to close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()