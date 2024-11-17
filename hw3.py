# Задание 1
from PIL.ImImagePlugin import number

names = ['Lena','Olga','Olga','Lena','Sasha','Egor','Lena','Igor']
name_count = {}

for name in names:
    count = names.count(name)
    name_count[name] = count
print(f'Словарь из имён и количества их повторений: {name_count}')

# Задание 2
numbers = [23,45,76,89,5]
sum_num = sum(numbers)
mult_num = 1

for number in numbers:
    mult_num = mult_num * number

sum_mult_num = {sum_num: mult_num}
print(f'Словарь из суммы элементов и их произведения: {sum_mult_num}')

# Задание 3
unique_names = []

for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(f'Список уникальных имён: {unique_names}\nКоличество элементов в этом списке: {len(unique_names)}')