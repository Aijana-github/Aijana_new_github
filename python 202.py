# Ищем в систему используя ЛОГИЧЕСКОЕ И
login = 'username'
password = '123456'
login1 = input("Введите имя пользователя: ")
password1 = input("Введите пароль: ")

if login1 == login and password1 == password:
    print('Вы вошли в систему!')
else:
    print('Не удаеься войти. Пожалуйста, проверьте правильность написания логина и пароля')