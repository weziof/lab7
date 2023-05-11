import json
import random

# Генератор випадкових чисел
random_generator = random.Random()

# Генеруємо рандомний ID
random_id = random_generator.randint(1, 100)

# Зберігаємо ID у змінну
id_variable = random_id

# Шлях до JSON файлу
json_file_path = "data.json"

# Завантажуємо JSON файл
with open(json_file_path) as file:
    data = json.load(file)

# Парсимо необхідні елементи з JSON
name = data["name"]
gender = data["gender"]
culture = data["culture"]

# Виводимо дані в консоль
print("ID:", id_variable)
print("Name:", name)
print("Gender:", gender)
print("Culture:", culture)
