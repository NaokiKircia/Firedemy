from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

#obsluga iframe - strona wewnatrz strony
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/iFrameTest.html")
driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\iFrameTest.html")
print("before window switch: " + (driver.find_element_by_tag_name('h1').text))
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
print("after window switch: " + (driver.find_element_by_tag_name('h1').text))
driver.switch_to.default_content()
print("and back to first window: " + (driver.find_element_by_tag_name('h1').text))
driver.close()

#klikanie na element i ustawianie wartosci pola tekstowego - za pomoca JavaScript
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/Test.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\Test.html")
wartosc = "Ola"
driver.execute_script("arguments[0].setAttribute('value', '" + wartosc + "')", driver.find_element_by_id("fname"))
driver.execute_script("arguments[0].click();", driver.find_element_by_id("newPage"))

#symulowanie podwojnego klikniecia myszki
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/DoubleClick.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\DoubleClick.html")
button = driver.find_element_by_id("bottom")
webdriver.ActionChains(driver).double_click(button).perform()
time.sleep(3)
driver.close()

#usuwanie danych z pola tekstowego - bo inaczej dopisuje do tego, co jest
driver.get("file:///C:/Users/algajews/Documents/Firedemy/Kurs_Selenium_Python/Selenium_part/Resources/Test.html")
# driver.get("file:///E:\Python Projects\Firedemy\Kurs_Selenium_Python\Selenium_part\Resources\Test.html")
username_input = driver.find_element_by_name("username")
username_input.send_keys("Ponury Adam")    #dopisuje
username_input.clear()
username_input.send_keys("Ponury Adam")
time.sleep(3)

#symulowanie klikniecia prawym przyciskiem myszki


#najechanie na element - hover\


#symulowanie drag i drop


#lancuchy akcji: najechanie na element i klikniecie


#upload pliku


#tworzenie screenshota - zrzut okna przegladarki



driver.quit()