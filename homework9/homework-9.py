import re

# Функция для разделения email на username и domain
def split_email(email):
    # Регулярное выражение для поиска имени пользователя и домена
    pattern = r'([^@]+)@([a-zA-Z0-9.-]+)'
    
    # Поиск соответствий с регулярным выражением
    match = re.match(pattern, email)
    
    if match:
        username = match.group(1)  # Первая группа - имя пользователя
        domain = match.group(2)    # Вторая группа - домен
        return username, domain
    else:
        return None, None  # Если email не соответствует формату

# Ввод email от пользователя
email = input("Введите ваш email: ")

# Разделение email
username, domain = split_email(email)

# Вывод результата
if username and domain:
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Неверный формат email.")