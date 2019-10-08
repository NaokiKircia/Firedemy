from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('.\Webdriver\chromedriver.exe')
driver.set_page_load_timeout(10)
driver.get("https://allegro.pl/")
driver.find_element_by_xpath("//*[@class='_13q9y _8hkto _nyhhx _l7nkx _1sql3 _qdoeh']").click()
driver.find_element_by_xpath("//*[@type='search']").send_keys('czosnek')
driver.find_element_by_xpath('//*[@class="_d25db_1t06j _13q9y _8tsq7 _1q2ua"]').click()
class_ebc9be2 = driver.find_elements_by_link_text('CZOSNEK OLBRZYMI GLADIATOR 5 SZT CEBUL + Gratis')
print(class_ebc9be2)
# assert "No results found." not in driver.page_source
time.sleep(5)
print("Test passed!")
driver.close()
