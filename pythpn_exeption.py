import requests

"""
try:
    блок,
    где возможна
    ошибка
except:
    действие
    в случае
    ошибки
finally:
    блок кода,
    который выполнится
    в любом случае
"""

# age = input('Enter the age: ')
# try:
#     if age < 18:
#         print('error')
#     else:
#         print('ok')
# except:
#     if age.isdigit():
#         if int(age) < 18:
#             print('error')
#         else:
#             print('ok')
#     else:
#         print('не число')

def send_data():
    data = {'name': 'Alex', 'age': 26}
    data = None
    return Exception('Error')

def get_data_from_server():
    try:
        data = send_data()
        print(data)
    except:
        data = []
        for i in data:
            print(i)


try:
    my_dict = {'name': 'dima'}
    if not my_dict.get('age'):
        print(my_dict.get('age'))
        raise Exception('Такого ключа нет!!') #raise - генерация собственного исключения


except Exception as err: # Обработка ошибки как переменной
    print(err) # Показывает текст ошибки. В случае со словарём - ключ, в котором возникла ошибка

age =250
def check_age(age):
    if age > 102:
        raise Exception('Возраст слишком большой')
    return age
try:
    print(check_age(226))
except:
    print('Возникла ошибка')

# HTTP
def get_page(url):
    try:
        response = requests.get(url)
        print(response.status_code)
        print(response.text) #text html
    except:
        print('Error')

url = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
get_page(url)