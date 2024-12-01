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