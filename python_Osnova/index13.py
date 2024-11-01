def createPurse(valuta, phone_number, name='неизвестный'):
    if valuta not in ('USD', 'KGS'):
        raise ValueError('только доллар или сом')
    return {
        'money': 0.00,
        'valuta': valuta,
        'name': name,
        'phone_number':phone_number
    }

def top_up_balance(purse, how_money):
    purse['money'] += how_money
    return how_money

def top_down_balance(purse, how_money):
    if purse['money'] - how_money < 0:
        print('Недостаточно средств')
        raise ValueError('Недостаточно средств')
    purse['money'] -= how_money
    print('Успешно сняли')
    return how_money

def info(purse):
    print(f"Владелец: {purse['name']} {purse['money']} {purse['valuta']} номер владельца счета: {purse['phone_number']}")
    
ji = createPurse('USD', 703010101, 'Ji')
milena = createPurse('KGS',999111222, 'Milena')
top_up_balance(ji, 100)
top_up_balance(milena, 100)
# info(milena)

    

# пиццерия
def will_order():
    answer = input('Вы хотите сделать заказ? (да/нет)')
    if answer =='да':
        return True
    else:
        print('Спасибо за заказ') 
        exit()


def choose_pizzas():
    menu = ['Маргарита','Пеперони','Гавайская','Охотничья',]
    basket = []
    print('Меню пицц: ')
    for pizza in menu:
        answer = input(f"Хотите {pizza}? (Да/Нет)").strip().lower()
        if answer =='да':
            basket.append(pizza)
            print(basket)
    if not basket:
        print("Вы не выбрали пиццы")
        answer = input("Хотите вернуться в меню или выйти (выберите 1 или 2)")
        if answer == '1':
            choose_pizzas()
        elif answer == '2':
            exit()
    return basket

def confirm_order(basket):
    print('Ваш заказ', basket)
    answer = input("Вы подтверждаете заказ (да/нет)?")
    if answer == 'да':
        return True
    elif answer =='нет':
        print("Давайте начнем заказывать")
        return False


def calculatePizza(basket):
    prices = {
        'Маргарита': 300,
        'Пеперони': 350,
        'Гавайская': 400,
        'Охотничья': 450
    }
    total = sum(prices[pizza] for pizza in basket)
    print(f'Ваш счет: {total} сом. Спасибо за покупку')


while True:
    if will_order():
        basket = choose_pizzas()
        if confirm_order(basket):
            calculatePizza(basket)
            break