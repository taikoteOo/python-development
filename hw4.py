# Задание 1. Пересечение спиков
def inter_list(list1: list, list2: list) -> list:
    inter = list(set(list1).intersection(list2))
    return inter

print(inter_list(list1 = [1,2,3,4], list2 =[2,4,6,8]))

# Задание 2. Симметрическая разность списков
def sym_diff_list(list1: list, list2: list) -> list:
    sym_diff = list(set(list1).symmetric_difference(list2))
    return sym_diff

print(sym_diff_list(list1 = [1,2,3,4], list2 =[2,4,6,8]))

# Задание 3. Строка в нижнем регистре
def down_str(up_str: str) -> str:
    return up_str.lower()

print(down_str('СтрОкА с РаЗнымИ рЕгИсТрАми'))

#Задание 4. Из списка в строку
def list_to_str(list1: list) -> str:
    return '---'.join(map(str, list1))

print(list_to_str(list1 = [1,2,3,4]))