username = 'user'
password = '123456'

def login(login,check_password):

    if password == check_password and login == username:
       print('Вы вошли в систему!')

    else:
      print('Пароли не совподают!')
login('user', '123456')
