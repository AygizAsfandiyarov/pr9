# Функция для ввода целого числа с обработкой ошибок
def get_input(num):
    while True:
        try:
            return int(input(num))  
        except ValueError:
            print("Ошибка. Пожалуйста, введите целое число.")

# Ввод чисел a и b с обработкой ошибок
a = get_input("Введите число a: ")
b = get_input("Введите число b: ")

# Проверка, что a меньше b, если нет, меняем их местами
if a > b:
    a, b = b, a


# Создание списка квадратов целых чисел между a и b
squares = [i**2 for i in range(int(a) + 1, (round(b)))]

# Вывод полученного списка
print("Список квадратов чисел между a и b:", squares)