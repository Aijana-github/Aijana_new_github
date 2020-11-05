products = {'gucci boots':10000,'chanel':20000,'adidas boots':8000,'nike sport-suit':23000,'nike boots':9000,'gucci sport-suit':24000,'lonsdale suit':8000,'dior chest':10000,
            'raben waist':15000,'wedding dress':500000}



username = 'school'
password = '1234567890qwerty'

def auth(login,password):

    if password == password and login == username and len(login) < 20 and not password.isdigit() and  not password.isalpha():



        return 'Вы вошли в систему'
    else:
         return 'Пароли совподают'
print(auth("school","1234567890qwerty"))
def counter(money,price):
    if money > price:
        result = money - price
        return result

    else:
        print("У вас недастоточно денег!")
print(counter(600,500))



def card():
    card_list = []
    for i in range(2):
        product = input()
        if product in products:
            card_list.append(product)
    return card_list

test_card = card()
for line in test_card:
    print(products[line])

def wallet(products)
    products(line)




