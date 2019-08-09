"""
Importowanie modułów
Generator liczb losowych
"""
import random

def generuj_liczbe(min, max):
    return random.randint(min, max)

for i in range(0,20):
    print(generuj_liczbe(0, 100))

"""
Instalacja paczek przez Pythona
xlrd - paczka pomagajaca przy czytaniu excela
"""

