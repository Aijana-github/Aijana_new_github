import random
product_list = ['asus', 'acer', 'iphone', 'samsung', 'intel hd',
                'nvidia', 'adata', 'kingston', 'macbook', 'xiomi',
                'iMac', 'amd', 'apacer']
def register(login,password,check_password):
    register_list = []
    if password == check_password:
        global code
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
    with open('product.txt','a') as file1:
        for product in product_list:
            file1.write(product+'\n')

write(product_list)
def sort_list():

    with open('product.txt') as file2:
        f2 = file2.readlines()

        for product in f2:
            product = product.strip()
            if product == 'acer' or product == "asus" or product == 'macbook' or product == 'iMac':
                file1 = open('computers.txt','a')
                file1.write(product+'\n')
            elif product == 'xiomi' or product == 'iphone' or product == 'samsung':
                file2 = open('phones.txt','a')
                file2.write(product+'\n')
            elif product == 'intel hd' or product == 'nvidia':
                file3 = open('video_card.txt','a')
                file3.write(product+'\n')
            elif product == 'adata' or product == 'apacer' or product == 'adata' or product == 'kingston':
                file4 = open('disc.txt','a')
                file4.write(product+'\n')
sort_list()
def open_file(filename:str):
    with open(filename) as f1:
        read_file = f1.read()
        return read_file
user_input = input("Варианты фильтрации: phones,computers,disc,video_card")
if user_input == 'phones':
    print(open_file('phones.txt'))
elif user_input == 'computers':
    print(open_file('computers.txt'))
if user_input == 'disc':
    print(open_file('disc.txt'))
elif user_input == 'video_card':
    print(open_file('video_card.txt'))

def activate(our_code,code):
    if our_code == code:
        print('Все хорошо!')
    else:
        print('Неверный код!')
print('Код, пришедший на почту',code)
our_code = list(input("Введите код для активации аккаунта: "))
true_code = []
for line in code:
    true_code.append(str(line))
activate(our_code, true_code)


def open_file(filename: str):
    with open(filename) as f1:
        f1_read = f1.read()
        return f1_read


def screen_input(user_input):
    if user_input == 'phones':
        print(open_file('phones.txt'))
    elif user_input == 'computers':
        print(open_file('computers.txt'))
    elif user_input == 'videocards':
        print(open_file('video_card.txt'))
    elif user_input == 'hdd':
        print(open_file('hdd.txt'))
    else:
        print('Вы ввели неверную категориб товара!')
screen_input('phones')

















































