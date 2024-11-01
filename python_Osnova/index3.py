# Типы данных
# str - string 
# int - integer
# float - 1.5
# bool - True False

# операторы сравнения
# > 
# <
# ==
# >=
# <=
# !=

# арифмет операторы
# +
# - 
# *
# /
# **
# //
# %

# строки
# name = 'алтынбек Балтабеков'
      # 0123456789
# print(name[9:19])
# индексы
# срезы[:::]
# [:::] begin end step


# Variable - Переменные
# itrunRooms1 = 'Edzen'
# itrunRooms2 = 'Kuma'
# itrunRooms1 = 'Edzen Oichiev' # переприсвоение
# print('добро пожаловать', itrunRooms1)
# print('хорошего вам пути', itrunRooms1)
# print('как вам наша едаб, дайте отзыв',itrunRooms1)
# print(itrunRooms2)
# firstName = input("введите ФИО:")
# age = int(input("введите ваш возраст:"))
# phoneNumber = int(input("введите ваш номер телефона:"))
# print(firstName, age, phoneNumber)


# условные операторы
# if - если
# elif - иначе если
# else - иначе
# если хотя бы одно условие уже сработало, то след не будет работать
# if условие 1:
#     то что будет работать при срабатывании условия
# elif условие 2:
#      вывод если условие получилось
# else:
#      конечный момент, если ничего из выше перечисленного не совпало по условию

# Дано два числа. Вывести на экран наибольшее из чисел;
# a = 25
# b = 25
# if a>b :
#     print('a')
# elif a<b:
#     print('b')
# else:
#     print('Равны')

# a = -20
# if a > 0 and a != 0:
#     print('positive')
# else:
#     print(abs(a))

# a = int(input('введите номер месяца '))
# if a == 1 or a == 12 or a == 2:
#     print('Зима') 
# elif a == 3 or a == 4 or a == 5:
#     print('Весна')  
# elif a in (6,7,8):
#     print('лето')

name = ' Кожомкул Баатыр '
print(name.lower())
print(name.upper())
print(name.capitalize())
name = name.replace('Кожомкул', 'Курманбек')
print(name.title())
print(name.strip())
print(name.split())
print(name.find('Баатыр'))