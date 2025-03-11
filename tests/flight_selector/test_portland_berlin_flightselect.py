import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import io
import sys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://blazedemo.com/")
        self.assertIn("BlazeDemo", driver.title)

        elem1 = driver.find_element(By.XPATH, '//select[@name="fromPort"]/option[text()="Portland"]')
        elem1.click()
        
        elem2 = driver.find_element(By.XPATH, '//select[@name="toPort"]/option[text()="Berlin"]')
        elem2.click()

        button1 = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        button1.click()

        # Wait for the next page to load
        time.sleep(3)

        self.assertIn("BlazeDemo - reserve", driver.title)

        header = driver.find_element(By.TAG_NAME, "h3")

        self.assertIn("Flights from Portland to Berlin", header.text, "Test Failed: Header did not contain the expected text.")


    def tearDown(self):
        self.driver.close()

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