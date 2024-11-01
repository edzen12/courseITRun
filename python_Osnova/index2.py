# name1 = input("ваше имя: ")
# name = 'Jas'
# Name = 'Beka'
# питон регистро зависимый
# нижний регистр = маленькие буквы
# верхний регистр = Большие буквы
   
# если переменные одинаковые, то сохраняется последняя
# код читается сверху вниз
# print(name+name)
# age = 45
# print(f'привет меня зовут {name1} [name] (name), мне {age}')
# когда мы складываем строки - это называется конкантенация, работает +

# input - встроенная функция питона, которая по умолчания принимает тип данных str 
# int() - встроенная функция, все что внутри он делает числом
# float() - встроенная функция, все что внутри он делает числом c остатком
# bool() - встроенная функция, все что внутри он делает True or False
# str() - встроенная функция, все что внутри он делает строкой


# firstNumber = int(input('введите число: ')) 
# secondNumber = int(input('введите число: '))
# print(firstNumber * secondNumber)

# операторы сравнения
# > больше
# < меньше
# == равно
# >= больше равно
# <= меньше равно
# != не равно
# = присвоение
# print(4>5)
# print(4<5)
# print(4>=5)
# print(4<=5)
# print(4!=5)
# print(4==5)



# if else elif  Условные операторы
# a = 'a' # бека говорит что в а больше б
# b = 'A' # никита говорит что в б больше а
# print(a>b)
# if b > a:
#     print("никита прав")
# if a > b:
#     print("бека прав")


# firstNumber = int(input("chislo: "))
# secondNumber = int(input("chislo: "))
# operator = input('введите + - * /:')
# if operator == '+':
#     print(firstNumber+secondNumber)
# elif operator == '-':
#     print(firstNumber-secondNumber)
# elif operator == '*':
#     print(firstNumber*secondNumber)
# elif operator == '/':
#     print(firstNumber/secondNumber)

# and 
# or

# проверку по возрасту для входа в клуб, ниже 18 лет мы будем говорить что "рано тебе", если человеку 18 лет, то говорим "заходите", если ему 60 то говорим "уже поздно"
# age = int(input("введите возраст:"))
# if age >=1 and age < 18:
#     print("рано тебе")
# elif age >= 18 and age < 60:
#     print("заходите")
# elif age >= 60 and age < 100:
#     print("уже поздно")
# else:
#     print("пишите правильно возраст!")


name = 'Маткеримов Матай Залкарович'
# индексы - своего номер каждого символа []
      # 0123456789
print(name[11]+name[12]+name[13]+name[14]+name[15])
# [:::] - срезы[:::]
# : begin - начало
# : end - конец
# : step - шаг
print(name[11:16])
print(name[11:])
print(name[:16])
print(name[0::2])