from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(r"..\drivers\chromedriver.exe")     zamiast pobierać webdriver [pip install webdriver_manager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\Test.html")
driver.maximize_window()
#narzedzie developerskie do odnajdywania elementow: F12
driver.find_element_by_id("newPage").click()
driver.close()
#metoda close zamyka tylko okno, na ktorym byl focus, a metoda quit zamyka wszystkie
