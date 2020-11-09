products = {'gucci boots':10000,'chanel':20000,'adidas boots':8000,'nike sport-suit':23000,'nike boots':9000,'gucci sport-suit':24000,'lonsdale suit':8000,'dior chest':10000,
            'raben waist':15000,'wedding dress':500000,'socks':6000,'paper':0}



username = 'school'
password = '1234567890qwerty'

def auth(login,password):

    if password == password and login == username and len(login) < 20 and not password.isdigit() and  not password.isalpha():



        return 'Вы вошли в систему'
    else:
         return 'Пароли совподают'
print(auth("school","1234567890qwerty"))
def counter(money,price):
    if money >= price:
        money = money - price
        return money

    else:
        return 'У вас недостаточно средств!'



def card():
    card_list = []
    for i in range(2):
        product = input('Введите товар: ')
        if product in products:
            card_list.append(product)
    return card_list

test_card = card()
def wallet(money):
    list_card = []
    for i in test_card:
        if money >= products[i]:
            money = counter(money, products[i])
            list_card.append(i)
    return {'Моя прихоть:': test_card, 'То что я смог купить: ': list_card,'сдача:': money}


print(wallet(50000))













