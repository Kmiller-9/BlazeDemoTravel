import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from parameterized import parameterized
import time
import io
import sys
import tempfile

class MultiFlightSelect(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver using webdriver-manager
        options = webdriver.ChromeOptions()
        # Use a temporary user data directory
        temp_user_data_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={temp_user_data_dir}")
        # Disable disk cache
        options.add_argument("--disable-application-cache")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    @parameterized.expand([
        ("Boston", "Buenos Aires"),
        ("Boston", "Rome"),
        ("Boston", "London"),
        ("Boston", "Berlin"),
        ("Boston", "New York"),
        ("Boston", "Dublin"),
        ("Boston", "Cairo"),
        ("Paris", "Buenos Aires"),
        ("Paris", "Rome"),
        ("Paris", "London"),
        ("Paris", "Berlin"),
        ("Paris", "New York"),
        ("Paris", "Dublin"),
        ("Paris", "Cairo"),
        # Add all other combinations here
    ])
    def test_form_submission(self, from_port, to_port):
        driver = self.driver
        # Navigate to BlazeDemo
        driver.get("https://blazedemo.com/")

        # Select departure city
        departure_city = driver.find_element(By.NAME, "fromPort")
        departure_city.send_keys(from_port)

        # Select destination city
        destination_city = driver.find_element(By.NAME, "toPort")
        destination_city.send_keys(to_port)

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Wait for the next page to load
        time.sleep(3)

        # Retry mechanism for handling rate limit
        retries = 3
        for _ in range(retries):
            if "Rate exceeded" not in driver.page_source:
                break
            time.sleep(5)  # Wait before retrying
            driver.refresh()

        # Check for a specific element on the resulting page to verify success
        expected_text = f"Flights from {from_port} to {to_port}"
        self.assertIn(expected_text, driver.page_source, f"Test Failed: {expected_text} not found in page source.")

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

if __name__ == "__main__":
    unittest.main()