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

def rzeczy(pierwsza_rzecz, *args):
    print(pierwsza_rzecz)
    print(args[0])
    for arg in args:
        print(arg)

rzeczy("lampa", "koc", "kanapa", "szafa")
