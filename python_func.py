# def hello(name):
#     print('Hello')
#     print_name(name)
#
# def main():
#     hello('Sasha')

def bye():
    print('Bye')

bye()

def print_name(name):
    print(name)

# name = 'Max'
# last_name = 'Dima'
# print_name(name='Taiko')
# print_name(name=name)
# print_name(name=last_name)


def print_info(name, lastname, age, city='SPb'): # Сигнатура - имя и параметры функции
    info = {
        'name': name,
        'lastname': lastname,
        'age': age,
        'city': city
    }
    return info

user_name = 'Dmitry'
user_lastname = 'Ivanov'
user_age = 32
user_city = 'Moscow'

# позиционные аргументы
print_info(user_name, user_lastname, user_age, user_city)

# именованные аргументы
print_info(name=user_name, age=user_age, city=user_city, lastname=user_lastname)

# комбинированный способ
print_info(user_name, user_lastname, user_age, city=user_city) #можно указать именной только в конце

print_info(name=user_name, age=user_age, lastname=user_lastname) #с дефолтным значением city

result = print_info(name=user_name, age=user_age, city=user_city, lastname=user_lastname)
print(result)

def hello(name):
    print('Hello')
    print_name(name)
    bye()

def main():
    hello('Sasha')

main()


def text_analise(text):
    """
    :param text='hello':
    :return: {'h':1, 'e':1, 'l':2, 'o':1}
    """
    stat = {}
    for s in text:
        stat[s] = text.count(s) # стичает количество раз, сколько встречается символ
    return stat

print(text_analise(text='hello'))

def text_to_list(text: str) -> list[str]: # Указыват тип данных аргумента -> тип данных результата[тип даннх элементов результата]
    return text.split() #разбивает строку по разделителю (по умолчанию пробел)

print(text_to_list(text='I love python string'))

emails = [
    'admin@mail.ru',
    'alex@yandex.ru',
    'alena@mail.ru',
    'igor@gmail.com'
]

def get_emails(in_emails: list[str], domen: str = '.ru') -> list:
    emails = []
    for email in in_emails:
        if email.endswith(domen): #кончается ли строка чем-то (.startswith() - начинается ли)
            emails.append(email)
    return emails

print(get_emails(in_emails=emails, domen='@yandex.ru'))

def check_age(age: int|str) -> bool:
    if isinstance(age, int): #является ли нужным типом данных
        if age < 18:
            return False
        else:
            return True
    if isinstance(age, str):
        if age.isdigit(): #проверяет, является ли строка числом
            if int(age) < 18:
                return False
            else:
                return True
        else:
            return False
    return False

age = 20
if check_age(age):
    print('ok')
else:
    print('error')