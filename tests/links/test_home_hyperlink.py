# Test Case to ensure user can click on the 'home' element at the top of the screen and be brought to a login screen 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

# Set up the WebDriver (e.g., Chrome)
service = Service(r'C:\WebDrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Open the web page
driver.get('https://blazedemo.com/index.php')
print("Site loaded")

# Wait for the page to load
time.sleep(2)

# User can click on the 'home' element at the top of the screen and be brought to a login screen 
link_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/a[3]" 
link = driver.find_element(By.XPATH, link_xpath)
link.click()
print("Home link clicked")

# Wait for the new page to load
time.sleep(2)

def test_example(self):
        driver = self.driver
        element = driver.find_element(By.ID, "email")  # Replace with your target element's locator
        self.assertEqual(element.text, "Expected Text", "Text does not match!")

def tearDown(self):
        self.driver.quit()