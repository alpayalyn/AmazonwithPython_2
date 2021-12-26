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

    def test_delete_item_from_cart(self):
        print("User should be able to delete an item from cart")
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
        time.sleep(3)
        self.assertTrue(self.driver.find_element_by_id("WLHUC_viewlist").is_displayed())
        time.sleep(3)
        self.driver.find_element_by_id("WLHUC_viewlist").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("wl-info-aa_add_to_cart")[1].click()
        time.sleep(3)        
        self.driver.find_element_by_id("nav-cart")
        cartCount=int(self.driver.find_element_by_id('nav-cart-count').text)        
        if(cartCount<1):
            print("Cart is empty")
            exit()            
        if(self.driver.title.startswith("Amazon.com Shopping Cart")):
            self.driver.find_element_by_class_name("sc-action-delete")[0].click()
            time.sleep(2)        
        # to confirm the item was delete successfully
        self.assertTrue(int(self.driver.find_element_by_id('nav-cart-count').text) < cartCount)        
 
    def tearDown(self):
        # to close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()