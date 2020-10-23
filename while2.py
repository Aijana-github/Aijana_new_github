user_name = 'maksim'
password = '123456'
i = 0
while i < 5:
    login = input("Введите имя пользователя:")
    check_password = input("Введите пароль: ")
    if login == user_name and check_password == password:
        print("Вы вошли в систему")
        break
    else:
        print("Вы ввели неверные данные!")
        i = + 1