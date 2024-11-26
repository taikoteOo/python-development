from functools import reduce
# def sum_numbers(a, b):
#     return a+b

# result = sum_numbers(5,4)
# print(result)

double = lambda x: x**2
print(double(2))

# def double(x):
#     return x**2

# Функции высшего порядка - функции, в качестве аргумента которых другие функции

list_of_numbers = ['1','234','234','22','11']

# list_int_numbers = []
# for i in list_of_numbers:
#     if i.isdigit():
#         list_int_numbers.append(int(i))
#
# print(list_of_numbers)
# print(list_int_numbers)

list_int_numbers = map(int, list_of_numbers)
list_duble_numbers = list(map(double, list_int_numbers)) # возвращает список
print(list_int_numbers) # возвращает итерируемый объект <map object at 0x000001C4197FD480>
print(list_duble_numbers)

list_duble_numbers_1 = list(map(lambda x: int(x)**2, list_of_numbers))
print(list_duble_numbers_1)

users = [['alex', 70], ['dima', 50], ['elena', 30], ['sveta', 25]]
# old_users = []
# for i in users:
#     if i[1] > 30:
#         old_users.append(i)
# print(old_users)

old_users = list(filter(lambda user: user[-1] > 30, users))
print(old_users)

# reduse возвращает только один элемент
sum_numbers = reduce(lambda x,y: int(x)+int(y), list_of_numbers)
print(sum_numbers)