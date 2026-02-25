
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com") # opens the URL

input("Press Enter to close browser...") # keeps the page opened
driver.quit() # quits the website after ENTER is pressed
