"""
Декоратонкция - функция которая позволяет изменять или расширять поведение другой функции или метода
"""
import time


def decorator(func): #функция - декоратор
    def wrapper(): #функция - обёртка
        print('before')
        func() #декорируемая функция
        print('after')
    return wrapper

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

def timing(func):
    def wrapper(*args, **kwargs):
        star = time.time() #текущее время от рождества в секундах
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения {end - star} сек.')
        return result
    return wrapper

@decorator #применение декоратора перед функцией
def hello():
    print('Hello')

@repeat(3)
def greet(name):
    print(f'Hello {name}')

@timing
def parse_page():
    time.sleep(3) #имитация временной задержки (перерывы в пограмме на указанное кол-во сек)

def memoize(func):
    cashe = {}
    def wrapper(*args):
        if args in cashe:
            return cashe[args]
        else:
            result = func(*args)
            cashe[args] = result
            return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# hello()
# greet(name='Alisa')
# parse_page()
start = time.time()
print(fibonacci(35))
end = time.time()
print(f'Время выполнения {end - start} сек.')