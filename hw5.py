# Задание 1. Сумма, произведение, минимум и максимум

def math_num(num1: int, num2: int, num3: int):
    sum_num = sum([num1, num2, num3])
    mult_num = num1 * num2 * num3
    min_num = min([num1, num2, num3])
    max_num = max([num1, num2, num3])
    return (f'Сумма чисел: {sum_num}\nПроизаедение чисел: {mult_num}'
            f'\nНаибольшее число: {max_num}\nНаименьшее число: {min_num}')

print(math_num(num1=35, num2=18, num3=22))

# Задание 2. Обработка строки
def fun_str (str1: str):
    list_of_str = str1.split(' ')
    word_count = len(list_of_str)
    more_2_let_count = 0
    for word in list_of_str:
        if len(word) > 2:
            more_2_let_count += 1
    down_str = str1.lower()
    up_str = str1.upper()
    return (f'Количество слов в строке: {word_count}\nКоличество слов, где больше двух символов: {more_2_let_count}'
            f'\nСтока в нижнем регистре: {down_str}\nСтрока в верхнем регистре: {up_str}')

print(fun_str('Это текст, Который МЫ проверяеМ'))

# Задание 3. Обработка списка
def fun_list(list1: list):
    unique_list = list(set(list1))
    more_25_list = []
    for num in unique_list:
        if num > 24:
            more_25_list.append(num)
    dict_num = {}
    for i in range(1,len(more_25_list)+1):
        dict_num[str(i)] = more_25_list[i-1]
    return (f'Уникальные значения списка: {unique_list}\nСписок, где числа больше 25: {more_25_list}'
            f'\nСловарь с элементами списка: {dict_num}')

print(fun_list([1,30,30,25,24,30,1,27,25,40]))

#Задание 4. Из сантиметров в метры
def sm_of_m(sm_num: int):
    m_num = sm_num/100
    return f'В {sm_num} самнтиметрах: {m_num} метра'

print(sm_of_m(24))

# Задание 5. Из минут в часы и минуты
def min_of_hours(mint: int):
    lust_min = int(str(mint)[-1])
    if lust_min == 1 and mint != 11:
        min_name = 'минута'
    elif 5 > lust_min > 1 and (mint < 10 or mint > 14):
        min_name = 'минуты'
    else:
        min_name = 'минут'
    if mint < 60:
        hours = f'{mint} {min_name}'
    else:
        int_hours = int(mint/60)
        last_hours = int(str(int_hours)[-1])
        if last_hours == 1 and int_hours != 11:
            hours_name = 'час'
        elif 5 > last_hours > 1 and (int_hours < 10 or int_hours > 14):
            hours_name = 'часа'
        else:
            hours_name = 'часов'
        int_min = mint - int_hours*60
        if 15 > int_min > 11:
            min_name = 'минут'
        hours = f'{int_hours} {hours_name} {int_min} {min_name}'
    return f'Заданное время: {hours}'

print(min_of_hours(672))

# Задание 6. Сумма и произведение цифр числа
def fun_3_num(nums: int):
    str_num = str(nums)
    list_num = []
    mult_num = 1
    for num in str_num:
        list_num.append(int(num))
        mult_num *= int(num)
    sum_num = sum(list_num)
    return f'Сумма чифр числа: {sum_num} \nПроизведение цифр числа: {mult_num}'

print(fun_3_num(864))

# Задание 7. Принадлежность числа промежутку
def num_line(x: int, a: int, b: int):
    if b > x > a:
        result = 'x принадлежит промежутку от a до b'
    else:
        result = 'x не принадлежит промежутку от a до b'
    return result

print(num_line(x=2, a=1, b=15))
print(num_line(x=16, a=1, b=15))

# Задание 8. Словарь из строк
def dict_from_str(str1: str, str2: str):
    dict_str = {}
    if len(str1) == len(str2):
        for i,j in zip(str1, str2):
            dict_str[i] = j
    return dict_str

txt1 = 'abcde'
txt2 = '12345'
print(dict_from_str(txt1,txt2))

# Задание 9. Данные пользователя в словарь
def users_date():
    user_name = input('Введите ваше ФИО: ')
    user_age = input('Введите ваш врозраст: ')
    if user_age.isdigit():
        user_age = int(user_age)
        if user_age < 1 or user_age > 150:
            print('Возраст не соответсвует заданному диопазону!')
            user_age = 0
    else:
        print('Возраст может быть только целым числом!')
        user_age = 0
    user_phone = input('Введите ваш номер телефона: ')
    if len(user_phone) < 4 or len(user_phone) > 11:
        print('Указан невозможный номер')
        user_phone = '8-000-000-00-00'
    user_date = {
        'ФИО': user_name,
        'Возраст': user_age,
        'Номер телефона': user_phone
    }
    return print(user_date)

users_date()

# Задание 10. Работа со строкой
def fun_str_2(str1: str):
    len_str = len(str1)
    fitst_el_str = str1[0]
    end_el_str = str1[-1]
    str_words = str1.split()
    first_word = str_words[0]
    end_word = str_words[-1]

    for i in range(1, len(str1)):
        if str1[i] == 'p':
            one_i = i
        if str1[i] == 'l':
            end_i = i-1
    pro = str1[one_i:end_i]
    return (f'Количество символов в строке: {len_str} \nПервый элемент строки: {fitst_el_str}'
            f'\nПоследний элемент строки: {end_el_str} \nПервое слово строки: {first_word}'
            f'\nПоследнее слово строки: {end_word} \nСрез строки: {pro}')

print(fun_str_2('Python is the best programming language'))

# Задание 11. Калькулятор
def calculator(operation, a, b):
    operations = ('add', 'subtract', 'multiply', 'divide')
    if operation == 'add':
        result = f'Сумма числе равна: {a+b}'
    elif operation == 'subtract':
        result = f'Разность числе равна: {a-b}'
    elif operation == 'multiply':
        result = f'Произведение числе равно: {a*b}'
    elif operation == 'divide':
        if b != 0:
            result = f'Кратное числе равно: {a/b}'
        else:
            result = 'Деление на ноль запрещено!'
    else:
        result = 'Неизвестная операцтия'
    return result

print(calculator(operation='add', a=2, b=5))
print(calculator(operation='subtract', a=2, b=5))
print(calculator(operation='multiply', a=2, b=5))
print(calculator(operation='divide', a=2, b=5))
print(calculator(operation='divide', a=2, b=0))
print(calculator(operation='not fun', a=2, b=5))
