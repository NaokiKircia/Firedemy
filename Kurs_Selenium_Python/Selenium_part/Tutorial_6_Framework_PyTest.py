import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

'''
- pip install pytest
- assert pozwala na sprawdzenie konkretnego warunku
- glupi interpreter ma problem z 2 pythonami:    python -m pytest Testname 
- puszcza wszystkie suity z pytestem
'''

# def test_method():
#     x = 5
#     y = 2
#     assert x + y == 7, "Assertion failed, Expected 7"
#     assert x + y == 2, "Assertion failed, Expected 7"

'''Weryfikacja rezultatow asercje
- mozna sprawdzac wszystko co zwraca True/False
'''
# driver = webdriver.Chrome(ChromeDriverManager().install())
def test_method():
    x = 5
    y = 2
    # assert driver.title == "Strona testowa", "Assertion failed, Expected 7"
    assert x + y == 7, "Assertion failed, Expected 7"
    assert x + y == 2, "Assertion failed, Expected 2 but was " + str(x + y)
