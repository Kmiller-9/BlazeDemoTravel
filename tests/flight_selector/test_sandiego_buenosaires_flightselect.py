import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import io
import sys

class SanDiegoBuenosAires(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_form_submission(self):
        driver = self.driver
        # Navigate to BlazeDemo
        driver.get("https://blazedemo.com/")

        # Example interaction: Select departure city
        departure_city = driver.find_element(By.NAME, "fromPort")
        departure_city.send_keys("San Diego")

        # Example interaction: Select destination city
        destination_city = driver.find_element(By.NAME, "toPort")
        destination_city.send_keys("Buenos Aires")

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Wait for the next page to load
        time.sleep(3)
        
        # Verify the header on the next page
        header = driver.find_element(By.TAG_NAME, "h3").text
        expected_header = "Flights from San Diego to Buenos Aires:"
        if header == expected_header:
            print("Header verification passed: Correct cities selected.")
        else:
            print(f"Header verification failed: Expected '{expected_header}', but got '{header}'.")
            
    def tearDown(self):
        # Close the browser
        self.driver.quit()

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