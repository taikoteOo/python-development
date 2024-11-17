# Задание 1
list_1 = [1,2,3,4,5]
list_2 = [3,4,5,6,7,8]
common_el = []
dif_el = []

for el_1 in list_1:
    for el_2 in list_2:
        if el_1 == el_2:
            common_el.append(el_1)
        else:
            if el_1 not in dif_el:
                dif_el.append(el_1)

print(f'Общие элементы списка: {common_el}')
print(f'Элементы, которые есть только в первом списке: {dif_el}')

# Задание 2
brand = input('Введите марку машины: ')
model = input('Введите модель машины: ')
year = input('Введите год выпуска машины: ')
color = input('Введите цвет машины: ')

car = {
    'brand': brand,
    'model': model,
    'year': year,
    'color': color
}
print(f'Список ключей: {list(car.keys())}')
print(f'Список значений: {list(car.values())}')
key_val = []
for key in car:
    key_val.append(f'{key} - {car[key]}')
print(f'Списк элементов: {key_val}')
