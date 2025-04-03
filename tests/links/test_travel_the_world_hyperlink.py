# Test Case to ensure user can click on the 'Travel The World' element at the top of the screen and be brought back to the Travel The World starting page of the site 
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import io
import sys

class TravelTheWorldHyperlink(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_travel_the_world_hyperlink(self):
        driver = self.driver
        # Open the web page
        driver.get('https://blazedemo.com/index.php')
        print("Site loaded")

        # Wait for the page to load
        time.sleep(2)

        # User can click on the 'Travel The World' element at the top of the screen and be brought back to the home page of the site 
        link_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/a[2]"
        link = driver.find_element(By.XPATH, link_xpath)
        link.click()
        print("Destination of the week link clicked")

        # Wait for the new page to load
        time.sleep(2)

        # Close the browser
        driver.quit()

    def run(self, result=None):
        # Create a string buffer to capture the output
        buffer = io.StringIO()
        # Redirect stdout to the buffer
        sys.stdout = buffer
        try:
            super().run(result)
        finally:
            # Reset stdout
            sys.stdout = sys.__stdout__
        # Store the output in the result object
        if result:
            result.output = buffer.getvalue()

if __name__ == '__main__':
    unittest.main()