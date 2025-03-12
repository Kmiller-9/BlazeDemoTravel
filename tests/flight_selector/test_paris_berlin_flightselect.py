import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import io
import sys

class TestParisBerlin(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_form_submission(self):
        driver = self.driver
        # Navigate to BlazeDemo
        driver.get("https://blazedemo.com/")

        # Example interaction: Select departure city
        departure_city = driver.find_element(By.NAME, "fromPort")
        departure_city.send_keys("Paris")

        # Example interaction: Select destination city
        destination_city = driver.find_element(By.NAME, "toPort")
        destination_city.send_keys("Berlin")

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Wait for the next page to load
        time.sleep(3)

        # Check for the header on the resulting page to verify success
        header = driver.find_element(By.TAG_NAME, "h3")
        self.assertIn("Flights from Paris to Berlin", header.text, "Test Failed: Header did not contain the expected text.")

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