list = [number for number in range(1,100,5)] 

# Находим индексы минимального и максимального элементов
min = list.index(min(list))
max = list.index(max(list))

# Меняем местами минимальный и максимальный элементы
list[min], list[max] = list[max], list[min]

print("Список после замены:", list)