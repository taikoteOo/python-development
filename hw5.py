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
