import random

# Генерация списка из 10 случайных чисел от 0 до 100
numbers = [random.randint(0, 100) for _ in range(10)]
print("Сгенерированный список:", numbers)

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        print(numbers[i])
