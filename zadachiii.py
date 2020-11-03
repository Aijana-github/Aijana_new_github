import random
product_list = ['asus', 'acer', 'iphone', 'samsung', 'intel hd',
                'nvidia', 'adata', 'kingston', 'macbook', 'xiomi',
                'iMac', 'amd', 'apacer']
def register(login,password,check_password):
    register_list = []
    if password == check_password:
        code = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9,0],4)
        register_list.append(login)
        register_list.append(password)
        return register_list
    else:
        return 'Пароли не совподают'
user = register('user','123456','123456')
username = user[0]
password = user[1]
def auth(login,password):

    if password == password and login == username:
        return 'Вы вощли в систему'
    else:
         return 'Пароли совподают'
print(auth("winter","123456"))
def write(product_list):
    with open('product.txt','w') as file1:
        for product in product_list:
            file1.write(product+'\n')

write(product_list)
def sort_list():
    with open('product.txt') as file2:
        f2 = file2.readlines()
        for product in f2:
            if product == 'acer' or product == "asus" or product == 'macbook' or product == 'iMac':
                file1 = open('computers.txt','w')
                file1.write(product)
            elif product == 'xiomi' or product == 'iphone' or product == 'samsung':
                file2 = open('phones.txt','w')
                file2.write(product)
            elif product == 'intel hd' or product == 'nvidia':
                file3 = open('video_card.txt','w')
                file3.write(product)
            elif product == 'adata' or product == 'apacer' or product == 'adata' or product == 'kingston':
                file4 = open('disc.txt','w')
                file4.write(product)




























