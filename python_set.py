# Множества set() - олько уникальные значения
numbers = {1,2,2,2,2,4,5}
print(type(numbers))
print(numbers)

numbers.add(6) #добавление элемента
numbers.remove(2) #удаление элемента
numbers.discard(10) #даление без ошибки

first_numbers = {1,2,3,4,5}
second_numbers = {4,5,6,7,8}

# oбъединение множеств
third_numbers = first_numbers.union(second_numbers)
print(third_numbers)
# | - оператор "или", объединяет множества
print(first_numbers | second_numbers)

# пересечение множеств
third_numbers = first_numbers.intersection(second_numbers)
print(third_numbers)

# разность множеств
third_numbers = first_numbers.difference(second_numbers)
print(third_numbers)
print(second_numbers - first_numbers)

# симметрическая разность - все элементы обоих множеств, за исключением общих
third_numbers = second_numbers.symmetric_difference(first_numbers)
print(third_numbers)
print(first_numbers ^ second_numbers)

# Замороженное множество - множество, которое нельзя изменить
frozent_numbers = frozenset(numbers)
print(type(frozent_numbers))