# Test Case to ensure user can click on the 'Travel The World' element at the top of the screen and be brought back to the home page of the site 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (e.g., Chrome)
service = Service(r'C:\WebDrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Open the web page on a different screen other than home page
driver.get('https://www.blazedemo.com/purchase.php')
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