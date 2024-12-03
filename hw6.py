from functools import reduce

# Применение map
list_for_map = ['2', '6', '4', '8', '6', '7']

duble_list = list(map(lambda x: int(x)*2, list_for_map ))
print(duble_list)

# Применение filter
list_big_num = list(filter(lambda x: x > 12, duble_list))
print(list_big_num)

# Применение reduce
mult_number = reduce(lambda x,y: x*y, duble_list)
print(mult_number)

# Обработка исключений
def error_one(num):
    try:
        if num < 0:
            raise Exception('Число меньше нуля!')
        result = f'Ваше число: {num}'
    except Exception as err:
        result = f'Ошибка: {err}'
    return result
print(error_one(-5))
print(error_one(5))

def error_two(num1, num2):
    try:
        def_num = num1/num2
        result = f'{num1}/{num2}={def_num}'
    except Exception as err:
        result = f'Ошибка: {err}'
    return result
print(error_two(5,0))
print(error_two(6,3))

def error_three(num):
    try:
        def_num = num/2
        result = f'Число {num} делйнное на два равно {def_num}'
    except Exception as err:
        result = f'Ошибка: {err}'
    return result
print(error_three(5))
print(error_three('5'))