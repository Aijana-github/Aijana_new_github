user_db = ''
password_db = ''
def register(username,password,repeat_password):
    if password == repeat_password:
        user_db = username
        password_db = password
        return user_db,password_db
    else:
        return 'Пароли не совподают'

print(register('maksim','123456','123456'))