# Функция AddRightDigit(D, K) добавляет к целому положительному числу K
# справа цифру D (0-9). Последовательно добавляем цифры D1 и D2
# к числу K, выводя результат каждого добавления.
def add_right_digit(d, k):
    return k * 10 + d


k = input("Введите целое положительное число K: ")
while type(k) != int:  # обработка исключений
    try:
        k = int(k)
        if k <= 0:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        k = input("Введите целое положительное число K: ")

d1 = input("Введите цифру D1 (0-9): ")
while type(d1) != int:
    try:
        d1 = int(d1)
        if not 0 <= d1 <= 9:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        d1 = input("Введите цифру D1 (0-9): ")

d2 = input("Введите цифру D2 (0-9): ")
while type(d2) != int:
    try:
        d2 = int(d2)
        if not 0 <= d2 <= 9:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        d2 = input("Введите цифру D2 (0-9): ")

k = add_right_digit(d1, k)
print("После добавления D1:", k)
k = add_right_digit(d2, k)
print("После добавления D2:", k)