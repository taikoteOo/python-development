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
age = input('Enter the age: ')
try:
    if age < 18:
        print('error')
    else:
        print('ok')
except:
    if age.isdigit():
        if int(age) < 18:
            print('error')
        else:
            print('ok')
    else:
        print('не число')

def send_data():
    data = {'name': 'Alex', 'age': 26}
    return data
def det_data_from_server():
    pass