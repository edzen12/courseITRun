# function
# функции делятся на 2:
#     1) встроенные функции питона
#         print(), abs(),int(), bool(),
#     2) пользовательские (которые мы пишем)
# def calc(num1, num2, simbol): # внутри скобок параметры
#     try:
#         if simbol == '+':
#             return num1+num2
#         if simbol == '-':
#             return num1-num2
#     except TypeError:
#         print("пишите числа")
# print(calc(4,2,'+'))# вызов функции для запуска

# def plus():
#     a = int(input('v: '))
#     b = int(input('v: '))
#     return f"{a+b}, otvet"

# print(plus())


# b = 45.6534535
# print(round(b,2))


def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1))

print(bonus_time(10000, False))





def abbrev_name(name):
    name = name.split()
    return f"{name[0][0].title()}.{name[1][0].title()}"


print(abbrev_name('Ji go'))




def points(games):
    count = 0
    for i in games:
        res = i.split(':')
        if res[0]>res[1]:
            count+=3
        elif res[0]== res[1]:
            count += 1
    return count



    
def reverse_words(s):
    str1 = ' '
    s = s.split()
    s.reverse() 
    
    return ' '.join(s)

print(reverse_words("hello world!"))