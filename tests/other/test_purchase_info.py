import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import io
import sys

class PurchaseInfo(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_form_submission(self):
        driver = self.driver
        # Navigate to BlazeDemo
        driver.get("https://blazedemo.com/purchase.php")

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

        # Check for a specific element on the resulting page to verify success
        if "Thank you for your purchase today" in driver.page_source:
            print("Test Passed: Form submitted successfully and confirmation page loaded.")
        else:
            print("Test Failed: Confirmation page did not load as expected.")

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