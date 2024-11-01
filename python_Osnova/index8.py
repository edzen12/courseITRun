try:
    num1 = int(input("введите число: "))
    num2 = int(input("введите число: "))
    simb = input("введите + - * / ")
    if simb == '+':
        print(num1+num2)
    elif simb == '-':
        print(num1-num2)
    else:
        print('вводите + или -') 
except ValueError:
    print("вводите только числа")