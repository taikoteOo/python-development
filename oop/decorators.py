"""
Декоратор - функция позволяющая изменять или расширять поведение другой функции или метода

"""

import time

# def decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#     return wrapper
#
# @decorator
# def hello():
#     print("Hello")
#
# hello()

def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

def timeing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения: {end - start} sec.")
        return result
    return wrapper


@decorator
def hello():
    print("Hello")

@repeat(3)
def greet(name):
    print(f"Hello, {name}")

@timeing
def parse_page():
    time.sleep(3)

def memorize(func):
    cash = {}
    def wrapper(*args):
        if args in cash:
            return cash[args]
        else:
            result = func(*args)
            cash[args] = result
            return result
    return wrapper

@memorize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n - 2)

# hello()
# greet(name="Alisa")
# parse_page()
start = time.time()
print(fibonacci(200))
end = time.time()
print(f"Время выполнения: {end - start} sec.")