# неизменяемые
# int, float, str, bool, tuple,frozenset 

# изменяемые типы данных
# list, dict, set-содержит уникальные значения

# индексы работают только с list, tuple, str 
# n = {3,4,5,3, 'hello', 'bro', 'hello'} # set - множества
# print(n)
# La = ['hello', 34, True, ('pipe', 'blic'), {12:'ji'}]


# Задача №1 - нужно объединить два списка, а повторяющиеся элементы выкинуть
list_names = ['Aza', 'Kuma', 'Bama', 'Anna', 'Vika']
get_names = ['Kuma', 'Anna', 'Adilet', 'Sasha']
list_names.extend(get_names)
print(set(list_names))

# Задача №2 - в строке нужно найти все числа и составить их в список
my_str = "frg5gth57ubdfh67 sbf4dsbdr0dxbf 2"
listPustoy = []
temp = ''
for i in my_str:
    if i.isdigit():
        temp+=i
    elif temp:
        listPustoy.append(int(temp))
        temp = '' # здесь идет обнуление temp чтобы дальше была проверка и они не сливались
print(listPustoy)