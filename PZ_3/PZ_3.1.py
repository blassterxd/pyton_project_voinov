# Даны три целых числа: A, B, C.
# Проверить истинность высказывания: «Число B находится между числами A и C».
a = input("Введите A: ")
while type(a) != int:  # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите A: ")

b = input("Введите B: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите B: ")

c = input("Введите C: ")
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print("Неправильно ввели!")
        c = input("Введите C: ")

if a < b < c or a > b > c:
    print("Да, число B находится между числами A и C")
else:
    print("Нет, число B не находится между числами A и C")
