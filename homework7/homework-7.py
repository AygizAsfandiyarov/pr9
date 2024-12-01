numbers = [number for number in range(5,150,11)] 
print("Список до сдвига:", numbers)

if numbers:  # Проверка на пустоту списка
    last_element = numbers[-1]  # Сохраняем последний элемент
    # Сдвигаем элементы вправо
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]
    numbers[0] = last_element  # Ставим последний элемент на первое место

print("Список после сдвига вправо:", numbers)