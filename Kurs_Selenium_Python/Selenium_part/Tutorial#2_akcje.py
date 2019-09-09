from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\Test.html")
# driver.find_element_by_id("clickOnMe").click()
driver.find_element_by_tag_name("p").click()
driver.close()