# Типы данных
# int 324
# float - 1.4
# str - 'string'
# bool - True
# list - списки [1,'hello', True]
# tuple - кортежи (1,'hello', True)
# tuple - почти во всем похож на list, но неизменяемый тип данных
# n = (1,'hello', True)
# n[1] = 'hello bro'
# print(n)
# dict - словари {key:value, key1: value1}
# изменяемый тип данных, с ключом и значением
# g = {
#     'Milena': 996771793888, 
#     'Ji':771700700, 
#     'Baltabkov Bolotbek':'холост'
#     }
# g['Baltabkov Bolotbek'] = 'Тешебеков Тешебай'
# print(g)
# set - множества {"бака", "балта", "камчы"}
# l = {"бака", "балта", "камчы"}
# print(l[0])






contactsNames = {
    'Milena Batyrbekova': 996771793888, 
    'Ji':771700700,  
    'Bayaman': 703703777,
    'Askar': 996773737332
}  
listOperators = {'999':'ошка', '555':"мегаком", '770':"билайн"}
while True:
    vybor = int(input("""Выберите действие:
        # 1 - поиск контакта
        # 2 - добавление нового контакта
        # 3- удаление контакта
            ваш выбор? """))
    if vybor == 1:
        searchName = input("name: ").title()
        if searchName in contactsNames.keys():
            print(searchName, contactsNames[searchName], 'найдена')
        else:
            print("не сущ", searchName)
    elif vybor == 2:
        AddName = input("name: ").title()
        if AddName in contactsNames.keys():
            print("уже есть такой контакт")
        else:
            addPhone = input("Phone Number: 996")
            if len(addPhone) ==9:
                contactsNames[AddName] = f"996{addPhone}"
                for i in listOperators:
                    if i == addPhone[0:3]:
                        print(listOperators[i])
            else:
                print("длина может быть от 9 до 13 символов в номере")
            print(contactsNames)
    elif vybor == 3:
        DelName = input("name: ").title()
        if DelName in contactsNames.keys():
            contactsNames.pop(DelName)
            print(contactsNames)
        else:
            print('нет такого контакта')
# создать программа которая спрашивает у пользователя 3 вида действий
# 1 - поиск контакта
#     если мы находим контакт, то выводим его с номером и именем
# 2 - добавление нового контакта
#     сделаем проверку на имя добавляемого контакта, если он есть, то предложим поменять имя и добавить или отказаться.
#     должна быть проверка на длину номера и на его корректность:
#           длина может быть 9  символов в номере
            # номер должен начинаться 996  и проверкой операторов на территории КР
# 3- удаление контака
    # делаем проверку на то, есть ли такой человек, если есть удаляем, а потом показываем всех контактов