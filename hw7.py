import os.path


# Задание 1. Информация о пользователях
def users_info():
    result = ''
    for i in range(1,4):
        user_name = input('Введите имя: ')
        user_lastname = input('Введите фамилию: ')
        user_phone = input('Введите номер телефона: ')

        result += (f'Пользователь {i}: \nИмя - {user_name} \nФамилия - {user_lastname}'
                  f'\nТелефон - {user_phone} \n---------------------\n')
    return result

if not os.path.exists('user_info'):
    os.makedirs(name='user_info', exist_ok=True)
if not os.path.exists('user_info/users.txt'):
    with open(file='user_info/users.txt', mode='w', encoding='utf-8') as user_info:
        user_info.write(users_info())
else:
    with open(file='user_info/users.txt', mode='a', encoding='utf-8') as user_info:
        user_info.write(users_info())

# Задание 2. Запись чисел по порядку
if not os.path.exists('numbers'):
    os.makedirs(name='numbers', exist_ok=True)
if not os.path.exists('numbers/numbers.txt'):
    with open(file='numbers/numbers.txt', mode='w', encoding='utf-8') as num:
        for i, j in zip(range(1, 11), range(10, 0, -1)):
            num.write(f'{i} {j}\n')
else:
    with open(file='numbers/numbers.txt', mode='a', encoding='utf-8') as num:
        for i, j in zip(range(1, 11), range(10, 0, -1)):
            num.write(f'{i} {j}\n')

# Задание 3. Работа с данными файла
num =  open(file='numbers/numbers.txt', mode='r', encoding='utf-8')
num_text = num.read().split('\n')
num_text.pop()
d = list(map(lambda numb: numb.split(), num_text))

def sum_numbers(num) -> str:
    result = 0
    for i in num:
        res = int(i[0]) * int(i[1])
        result += res
    return f'{result}'

def one_col(num):
    result = []
    for i in num:
        result.append(f'{i[0]}')
    return str(result)

if not os.path.exists('numbers/numbers_result.txt'):
     with open(file='numbers/numbers_result.txt', mode='w', encoding='utf-8') as num:
         num.write(sum_numbers(d) + '\n')
         num.write(one_col(d))
