username_list = []
password_list = []

i = 1

while i <= 5:
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    username_list.append(username)
    password_list.append(password)
    print(f'Пользователь под номером {i} зарегистрирован')
    i = i + 1
print(username_list)
print(password_list)
    
