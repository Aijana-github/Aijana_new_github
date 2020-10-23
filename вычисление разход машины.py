path = 200

v = int(input("Введите обьем бензобака: ")) # обьем бензобака в данное время

result = path / 100
fuel = v -(result*12)

if fuel > 1:
    print(f'Вы доехали до места назначения у вас осталось: {round(fuel)} литр(а) бензина')
else:

    result = 100 / 12
    result = result * v
    print(f'У вас закончится бензина на {round(result1)} километре!')