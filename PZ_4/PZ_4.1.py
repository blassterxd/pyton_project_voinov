# Даны два целых числа A и B (A < B).
# Найти произведение всех целых чисел от A до B включительно.
a = input("Введите A: ")
while type(a) != int:  # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите A: ")

b = input("Введите B (больше A): ")
while type(b) != int:
    try:
        b = int(b)
        if a >= b:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите B (больше A): ")

p = 1
i = a
while i <= b:
    p *= i
    i += 1

print("Произведение:", p)