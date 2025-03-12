import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import io
import sys

class SanDiegoLondonEtoE(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_form_submission(self):
        driver = self.driver
        # Navigate to BlazeDemo
        driver.get("https://blazedemo.com/")

        # Select the departure city
        departure_dropdown = Select(driver.find_element(By.NAME, "fromPort"))
        departure_dropdown.select_by_visible_text("San Diego")
        print("Departure city selected")

        # Select the destination city
        destination_dropdown = Select(driver.find_element(By.NAME, "toPort"))
        destination_dropdown.select_by_visible_text("London")
        print("Destination city selected")

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        print("Test Passed: Form submitted successfully and ticket page loaded.")

        # Wait for the new page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-small")))

        # Click on the button with the class 'btn btn-small'
        button_css_selector = ".btn.btn-small"
        try:
            button = driver.find_element(By.CSS_SELECTOR, button_css_selector)
            button.click()
            print("Flight selected")
        except Exception as e:
            print(f"Error: {e}")

        # Fill in the input fields
        driver.find_element(By.ID, "inputName").send_keys("John Doe")
        driver.find_element(By.ID, "address").send_keys("123 Main St")
        driver.find_element(By.ID, "city").send_keys("Anytown")
        driver.find_element(By.ID, "state").send_keys("CA")
        driver.find_element(By.ID, "zipCode").send_keys("12345")

        # Select the card type from the dropdown
        card_type_dropdown = Select(driver.find_element(By.ID, "cardType"))
        card_type_dropdown.select_by_visible_text("Visa")

        # Fill in the remaining input fields
        driver.find_element(By.ID, "creditCardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "creditCardMonth").clear()
        driver.find_element(By.ID, "creditCardMonth").send_keys("12")
        driver.find_element(By.ID, "creditCardYear").clear()
        driver.find_element(By.ID, "creditCardYear").send_keys("2026")
        driver.find_element(By.ID, "nameOnCard").send_keys("John Doe")

        # Tick the 'Remember me' checkbox
        remember_me_checkbox = driver.find_element(By.ID, "rememberMe")
        if not remember_me_checkbox.is_selected():
            remember_me_checkbox.click()

        # Click the 'Purchase Flight' button
        purchase_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        purchase_button.click()
        print("Flight purchased")

        # Wait for the confirmation page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        print("Confirmation page loaded")

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