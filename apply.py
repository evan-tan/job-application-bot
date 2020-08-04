from parameters import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def load_browser(browser_name):
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir=" + PROFILE[browser_name])
        driver = webdriver.Chrome(WEBDRIVER_PATH[browser_name], options=chrome_options)
        driver.get(PORTAL["glassdoor"])
        search = driver.find_element_by_id("sc.keyword")
        search.send_keys("Software engineering intern")
        search.send_keys(Keys.RETURN)

if __name__ == "__main__":
    load_browser("chrome")
    
# Close current tab
# driver.close()
# Close window
# driver.quit()