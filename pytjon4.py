money = int(input("Введите вашу сумму: "))

boots = 3000
wear = 4500
scarf = 900

product = input("Введите товар для покупки (boots wear scarf)")
if product == 'boots':
    if money >=boots:
        print('Спасибо за покупку')
    else:
        print('У вас недостаточно средств!')


elif product == 'wear':
    if money >=wear:
        print('Спасибо за покупку')
    else:
        print('У вас недостаточно средств!')


if product == 'scarf':
    if money >=scarf:
        print('Спасибо за покупку')
    else:
        print('У вас недостаточно средтсв!')
elif product == 'all':
    result = boots + wear + scarf
    if money >= result:
        print('Спасибо за покупку!')
    else:
        print('У вас недостаточно средств выберите что-то одно!')






