# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the youtube.com homepage
driver.get("https://www.youtube.com")
time.sleep(2)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("name","search_query")
search_bar.send_keys("IRCC")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "IRCC" in driver.title

# Selecting a vedio "new PR pathway " from the search results
vedio_link = driver.find_element("xpath","//yt-image/img")
vedio_link.click()


# Waiting for the laptop details page to load
time.sleep(8)

# Click on Share Button
Share_button = driver.find_element("xpath","//yt-button-view-model/button-view-model/button/yt-touch-feedback-shape/div/div[2]")
Share_button.click()

# Waiting for the Share to update
time.sleep(5)

# Clicking on copy link button
copy_button = driver.find_element("xpath","//yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
copy_button.click()
time.sleep(3)

# Closing the webdriver
driver.close()
