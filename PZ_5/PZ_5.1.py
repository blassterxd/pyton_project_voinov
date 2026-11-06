# Найти сумму чисел ряда 1, 2, 3, 4, ... от числа n до числа m.
# Суммирование оформлено функцией с параметрами.
def sum_range(n, m):
    s = 0
    i = n
    while i <= m:
        s += i
        i += 1
    return s


n = input("Введите n: ")
while type(n) != int:  # обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите n: ")

m = input("Введите m (не меньше n): ")
while type(m) != int:
    try:
        m = int(m)
        if m < n:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        m = input("Введите m (не меньше n): ")

print("Сумма:", sum_range(n, m))