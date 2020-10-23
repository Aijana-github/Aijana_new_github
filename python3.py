money = int(input("Введите вашу сумму: "))

product_price = 3000

if money > product_price:
    result = money - product_price
    print('Ваша сдача: ',result)
elif money == product_price:
    print('Спасибо за покупку!')
else:
    print('У вас недостаточно средств')