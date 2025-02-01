print(type(1/2))

my_var = [1,2,3,None,(),[],]
print(len(my_var))

my_var =  {"user", "bill", "password", "hillary"}
print(type(my_var))


def f(a, *pargs, **kargs):
    print(a, pargs, kargs)
f(1, 2, 3, x=4, y=5)

def function(name, *args, **kwargs):
   result = f"{name} {args[1]}....{kwargs['age']}"
   return result
print(function('Vlad', 'Petr', 'Ivan', lastname='Ivanov', age=18))

for i in range(5):
     if i % 2 == 0:
          continue
     print(i)

d = lambda p: p * 2
t = lambda p: p * 3
x = 2
x = d(x)
x = t(x)
x = d(x)
print(x)

try:
    raise IndexError
except IndexError:
    print('Получено исключение.')
else:
    print('Но в этом нет ничего страшного.')

numbers = [2, 1, 3, 4, 7]
more_numbers = [*numbers, 11, 18]
print(*more_numbers)

T = (4, 2, 3)
T = (1,) + T[1:]
print(T)

print(id(T))
text = 'Но в этом нет ничего страшного'
list_t = text.split(' ')
print(' '.join(list_t))

name = "snow storm"
print(name[6:8])
