import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import io
import sys

class BostonNewYorkEtoE(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_form_submission(self):
        driver = self.driver
        # Navigate to BlazeDemo
        driver.get("https://blazedemo.com/")

        # Example interaction: Select departure city
        departure_city = driver.find_element(By.NAME, "fromPort")
        departure_city.send_keys("Boston")

        # Example interaction: Select destination city
        destination_city = driver.find_element(By.NAME, "toPort")
        destination_city.send_keys("New York")

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Wait for the next page to load
        time.sleep(3)

        # Check for the header on the resulting page to verify success
        header = driver.find_element(By.TAG_NAME, "h3")
        self.assertIn("Flights from Boston to New York", header.text, "Test Failed: Header did not contain the expected text.")

        # Select the first flight (Virgin America 43)
        first_flight = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[1]/input")
        first_flight.click()

        # Wait for the next page to load
        time.sleep(4)
        
       # Check for the header on the resulting page to verify success
        header = driver.find_element(By.TAG_NAME, "h2")
        self.assertIn("Your flight from TLV to SFO has been reserved", header.text, "Test Failed: Header did not contain the expected text.")
        
        # Example interaction: Enter Name
        customer_name = driver.find_element(By.NAME, "inputName")
        customer_name.send_keys("Testy McTester")

        # Example interaction: Enter Address
        customer_address = driver.find_element(By.NAME, "address")
        customer_address.send_keys("Tester Address")

        # Example interaction: Enter City
        customer_city = driver.find_element(By.NAME, "city")
        customer_city.send_keys("Testing City")

        # Example interaction: Enter State
        customer_state = driver.find_element(By.NAME, "state")
        customer_state.send_keys("Testers State")

        # Example interaction: Enter Zip Code
        customer_zip = driver.find_element(By.NAME, "zipCode")
        customer_zip.send_keys("54321")

        # Example interaction: Enter Card Type
        customer_ccard_type = driver.find_element(By.NAME, "cardType")
        customer_ccard_type.send_keys("Visa")

        # Example interaction: Enter Credit Card Number
        ccard_number = driver.find_element(By.NAME, "creditCardNumber")
        ccard_number.send_keys("1111111111111111")

        # Example interaction: Enter Credit Card Expiry Month
        expirymonth = driver.find_element(By.NAME, "creditCardMonth")
        expirymonth.send_keys("January")

        # Example interaction: Enter Credit Card Expiry Year
        expiryear = driver.find_element(By.NAME, "creditCardYear")
        expiryear.send_keys("1401")

        # Example interaction: Enter Credit Card Name on Card
        ccard_name = driver.find_element(By.NAME, "nameOnCard")
        ccard_name.send_keys("Testy McTester")

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Wait for the next page to load
        time.sleep(4)

        # Print the page source for diagnosis
        page_source = driver.page_source
        print("Page Source:\n", page_source)

        # Check for the title to verify success
        expected_title = "BlazeDemo Confirmation"
        actual_title = driver.title
        self.assertEqual(expected_title, actual_title, "Test Failed: Confirmation page did not load as expected.")
        print("Confirmation page loaded with correct title")

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