def translater():
    print(f"Выберите правильный ответ как переводится кошка: {['cat','apple']}")
    answer = input("Введите ответ: ")
    if answer == 'cat':
        print('Вы ввели правильно!')
    else:
        print('Неправильно!')

translater()
