import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ViewProductDetails(unittest.TestCase):
    search_term="Samsung"
    base_URL="https://www.amazon.com"
    login_mail = "alpaylui78@gmail.com"
    login_password = "itsacoolpassword"

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
        self.driver.maximize_window()

    # --- Steps for AMZN_Search_TC_001 ---
    def test_AMZN_Search_TC_001_load_home_page(self):      
        print("User lands on the Home Page")
        driver=self.driver
        driver.get(self.base_URL)        
        self.assertIn("Amazon",driver.title)

    # --- Steps for AMZN_Search_TC_002 ---
    def test_AMZN_Search_TC_002_search_for_a_term(self):
        print("User searches for specific Text and navigates there.")
        self.driver.get(self.base_URL)         
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)
        self.assertIn(self.search_term,self.driver.title)
        self.assertNotIn("No results found.",self.driver.page_source)   
        
    # --- Steps for AMZN_Search_TC_003 ---
    def test_AMZN_Search_TC_003_add_item_to_wishlist(self):
        print("Open product")
        self.driver.get(self.base_URL)         
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)
        self.assertIn(self.search_term,self.driver.title)
        self.assertNotIn("No results found.",self.driver.page_source)   
        time.sleep(3)
        self.driver.find_elements_by_class_name("aok-relative")[1].click()

            # --- Steps for AMZN_Search_TC_004 ---
    def test_AMZN_Search_TC_004_delete_item_from_cart(self):
        print("User should be able to delete an item from cart")
        self.driver.get(self.base_URL)         
        searchTextBox=self.driver.find_element_by_id("twotabsearchtextbox")
        searchTextBox.clear()
        searchTextBox.send_keys(self.search_term)
        searchTextBox.send_keys(Keys.RETURN)
        self.assertIn(self.search_term,self.driver.title)
        self.assertNotIn("No results found.",self.driver.page_source)   
        time.sleep(3)
        self.driver.find_elements_by_class_name("aok-relative")[1].click()
        time.sleep(3)
        self.driver.find_element_by_id("wishlistButtonStack").click()
        time.sleep(3)
        loginTextBox = self.driver.find_element_by_id("ap_email")
        loginTextBox.clear()
        loginTextBox.send_keys(self.login_mail)
        self.driver.find_element_by_id("continue").click()
        time.sleep(3)      
        passwordTextBox = self.driver.find_element_by_id("ap_password")
        passwordTextBox.clear()
        passwordTextBox.send_keys(self.login_password)
        passwordTextBox.send_keys(Keys.RETURN)
        self.driver.find_element_by_id("auth-signin-button").click()
        time.sleep(3)      
        self.driver.find_element_by_id("wishlistButtonStack").click()
        time.sleep(3)       
        self.assertTrue(self.driver.find_element_by_id("WLHUC_viewlist").is_displayed())
        time.sleep(3)
        self.driver.find_element_by_id("WLHUC_viewlist").click()
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
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()