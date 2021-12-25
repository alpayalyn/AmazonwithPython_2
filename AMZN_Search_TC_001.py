import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver


baseURL = "http://www.amazon.com"
driver = webdriver.Chrome(executable_path="C:/seleniumdriver/chromedriver")
driver.maximize_window()
driver.implicitly_wait(10) #10 is in seconds
driver.get(baseURL)
assert "Amazon" in driver.title
driver.close()