import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import io
import sys

class DestinationOfTheWeek(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_destination_of_the_week(self):
        driver = self.driver
        # Open the web page
        driver.get('https://blazedemo.com/index.php')
        print("Site loaded")

        # Wait for the page to load
        time.sleep(2)

        # Validate the link with the text "destination of the week! The Beach!" works as expected
        link_xpath = "//a[contains(text(), 'destination of the week! The Beach!')]"
        link = driver.find_element(By.XPATH, link_xpath)
        link.click()
        print("Destination of the week link clicked")

        # Wait for the new page to load
        time.sleep(4)

        # Validate the title of the new page
        self.assertIn("BlazeDemo - vacation", driver.title)

        # Navigate back to the original page
        driver.back()
        print("Navigated back to the home page")

        # Validate return to home page
        self.assertIn("BlazeDemo", driver.title)

        # Wait for the page to load again
        time.sleep(2)

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