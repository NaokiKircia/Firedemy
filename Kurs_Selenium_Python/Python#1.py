"""
Notatki do kursu
1) Petla While
"""
# print("while loop examples")
#
# index = 0
# while index < 10:
#     print(index)
#     index += 1
#     if index == 2:
#         continue
#     if index == 8:
#         break
#     print("po ifie")

"""
2) Petla For
"""
# print("for loop examples")

# for number in range(10):
#      print(number)
#
# print("for od liczby")
# for number in range(5, 10):
#      print(number)
#
# print("for od liczby, z przskokiem")
# for number in range(2, 10, 3):
#      print(number)

# for character in "Bartek":
#     print(character)

"""
3) Metoda
"""
# def pogoda():
#     print("Jest slonecznie")
#     print("Temp jest wysoka")
#     print("Nie pada deszcz")
#
# pogoda()
#
# def przedstaw_sie(imie, wiek):
#     print("Czesc, jestem " + imie)
#     print("Mam " + wiek)
#
# przedstaw_sie("Ola", "28 lat")


"""
4) Args
"""
# def rzeczy(pierwsza_rzecz, *args):
#     print(pierwsza_rzecz)
#     print(args[0])
#     for arg in args:
#         print(arg)
#
# rzeczy("lampa", "koc", "kanapa", "szafa")

"""
5) Kwargs
- dziala na zasadzie slownika: klusz:vartosc
"""
# def dziennik(klasa, **kwargs):
#     print("Klasa " + klasa)
#     for nazwisko in kwargs.keys():
#         print(nazwisko)
#     print(kwargs.get("Kowalski"))
#
# dziennik("3c", Kowalski = "1", Nowak = "2", Wisniewski = "3")

"""
6) Zbiory
- add dziala tylko na unikalnych elementach
"""
# pierwszy_zbior = {"Warszawa", "Kieflce", "Poznan", "Lodz"}
# drugi_zbior = {"Warszawa"}
#
# pierwszy_zbior.add("Katowice")
# print(pierwszy_zbior)
# pierwszy_zbior.add("Kielce")
# print(pierwszy_zbior)
# print("operacje na zbiorach")
# print(pierwszy_zbior - drugi_zbior)
# print(pierwszy_zbior | drugi_zbior)
# print(pierwszy_zbior & drugi_zbior)
# print(pierwszy_zbior ^ drugi_zbior)

"""
6) Wyjatki
"""
# while True:
#     try:
#         print("Podaj pierwsza liczbe ")
#         pierwsza_liczba = int(input())
#         print("Podaj druga liczbe ")
#         druga_liczba = int(input())
#         print(pierwsza_liczba + druga_liczba)
#         break
#     except ValueError:
#         print("Podales bledna wartosc")
#         print("Sprobuj jeszcze raz")
#         continue

"""
7) Czytanie pliku
"""
file = open("plik_txt_#1.txt")
zawartosc = file.read()
print(zawartosc)
file.close()

file = open("plik_txt_#1.txt")
zawartosc = file.readlines()
print(zawartosc)
file.close()

file = open("plik_txt_#1.txt")
zawartosc = file.readline()
print(zawartosc)
file.close()

file = open("plik_txt_#1.txt")
for line in file:
    print(line)

"""
8) Zapisywanie do pliku
"""
file = open("zapis_do_pliku_#1.txt", "w")    #w-write
file.write("To jest jakis tekst")
file.close()

file = open("zapis_do_pliku_#1.txt", "w")
file.write("Calkiem inny tekst")
file.close()

file = open("zapis_do_pliku_#1.txt", "a")   #a-append
file.write(" Dodaj tekst do istniejacego")
file.close()

"""
9) Klasy
"""

class Pies:
    gatunek = 'pies domowy'

    def __init__(self, rasa, imie, wiek):
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

reksio = Pies('kundelek', 'Reksio', 2)
print(reksio.wiek)
print(reksio.imie)
print(reksio.rasa)
print(reksio.gatunek)
print(Pies.gatunek)
