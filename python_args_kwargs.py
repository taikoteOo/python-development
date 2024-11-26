def get_ingo(name, age=34):
    print(name.title()) # строка с большой буквы
    print(age)

get_ingo(name='alex')

# * - опретор распаковки/упаковки

a = [1,2,3]
b = [a, 4,5,6] # [[1, 2, 3], 4, 5, 6]
c = [*a, 4,5,6] # [1, 2, 3, 4, 5, 6]
print(b)
print(c)

def print_scorse(name, *scores):
    print(f'name - {name}')
    for i in scores:
        print(i)

print_scorse('dima', 26, 27, 56, 23)

def func(*args, **kwargs):
    # *args - неизвестное кол-во позиционных арументов
    # **kwargs - неизвесное кол-во именовных элементов
    pass # заглушка (тут будет код)

def print_pet_names(owner, **pets):
    print(f'Владелец - {owner}')
    """
    dog - Tima
    cat - Barsik
    """
    # print(f'Dog - {pets['dog']}\nCat - {pets['cat']}')
    for key, value in pets.items():
        print(f'{key} - {value}')

print_pet_names(owner='Dima', dog='Tima', cat='Barsik') #cобрался словарь