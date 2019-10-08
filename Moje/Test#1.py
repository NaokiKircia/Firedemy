from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./../Kurs_Selenium_Python/drivers/chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(5)
driver.close()
