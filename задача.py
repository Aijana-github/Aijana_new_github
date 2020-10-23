bmw = 20
merc = 18
fit = 9
fuel = int(input("Заправьте автомобиль: "))
i = 0
while i < 3:
    auto = input("Введите наименование автомобиля для тестирования: ")
    result = 0
    final =0
    path = 240
    if auto == 'bmw':
        result = path /100
        result = bmw * result # кол-во литров расхода поездки на И-К
        final = fuel - result
        if final > 0:
            print(f'После поездки остаток: {final} литров')
        else:
            result= 100 // bmw # расход 1 литра на % км
            result = result * fuel
            path = path -result
            print(f'Вам осталось ехать: {path} км')
    elif auto == 'merc':
        result = path / 100
        result = merc * result # кол-во литров расхода поездки на И-К
        final = fuel - result
        if final > 0:
            print(f'После поездки остаток: {final} литров')
        else:
            result = 100 / merc # расход 1 литра на % км100
            result = result * fuel
            path = path - result
            print(f'Вам осталось ехать: {round(path)}')
    elif auto == 'fit':
        result = path / 100
        print(result)
        result = fit * result # кол-во литров рахода поездки на И-К
        print(result)
        final = fuel - result
        if final > 0:
            print(f'После поездки остаток: {final} литров')
        else:
            result = 100 // fit  # расход 1 литра на % км
            print(result)
            result = result * fuel
            print(result)

            path = path - result
            print(f'Вам остлось ехать: {path}')
    i = i + 1

