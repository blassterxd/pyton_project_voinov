# Единицы массы: 1 - килограмм, 2 - миллиграмм, 3 - грамм, 4 - тонна, 5 - центнер.
# Дан номер единицы (1-5) и масса тела в этих единицах. Найти массу в килограммах.
n = input("Введите номер единицы массы (1-5): ")
while type(n) != int:  # обработка исключений
    try:
        n = int(n)
        if not 1 <= n <= 5:
            raise ValueError
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите номер единицы массы (1-5): ")

m = input("Введите массу тела: ")
while type(m) != float:
    try:
        m = float(m)
    except ValueError:
        print("Неправильно ввели!")
        m = input("Введите массу тела: ")

if n == 1:
    kg = m
elif n == 2:
    kg = m / 1000000
elif n == 3:
    kg = m / 1000
elif n == 4:
    kg = m * 1000
else:
    kg = m * 100

print("Масса в килограммах:", kg)