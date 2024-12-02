import random
ticket = [ 
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10], 
    [11, 12, 13, 14, 15], 
    [16, 17, 18, 19, 20], 
    [21, 22, 23, 24, 25]
]
# Функция для получения ввода пользователя
def get_user_choices():
    user_choices = []
    for i, row in enumerate(ticket):
        while True:
            try:
                # Запросить выбор числа от пользователя
                choice = int(input(f"Выберите число из строки {i+1} ({row}): "))
                if choice in row:
                    user_choices.append(choice)
                    break
                else:
                    print(f"Число {choice} не входит в выбранную строку.")
            except ValueError:
                print("Пожалуйста, введите правильное число.")
    return user_choices

# Функция для случайного выбора чисел
def get_random_choices():
    random_choices = [random.choice(row) for row in ticket]
    return random_choices

# Вывод статистики
def print_statistics(user_choices, random_choices):
    print(f"\nВаши выбранные числа: {user_choices}")
    print(f"Случайно выбранные числа: {random_choices}")
    
    # Подсчитаем совпадения
    matches = len(set(user_choices) & set(random_choices))
    print(f"Количество совпадений: {matches}")

# Основная функция
def main():
    print("Добро пожаловать в лотерею!")
    user_choices = get_user_choices() # Получаем выбор пользователя
    random_choices = get_random_choices()# Получаем случайный выбор
    print_statistics(user_choices, random_choices)  # Выводим статистику
# Запуск приложения
if __name__ == "__main__":
    main()