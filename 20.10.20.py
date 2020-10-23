product_list = ['bread','cheese','egg','meat']
cook_list = []
print('У вас имеются такие продукты: ',product_list)
product = input("Возьмите продукт: ")
i = 0
while product != '0' and i <= len(product_list):
    if product in product_list:
        cook_list.append(product)
    else:
        print('Используйте продукты из тарелки!')
    product =input("Возьмите продукт: ")
    i = i + 1
j = 0
buter = ['bread', 'cheese']
biff = ['meat', 'egg']
ham = ['bread', 'egg', 'meat']
ch_ham = ['bread', 'cheese', 'egg', 'meat']
if len(cook_list) == len(buter):
    j = 0
    while j < len(cook_list):
        if cook_list[j] in buter:
            j = j + 1
        else:
            print('Вы дали мне не тот продукт')
            break
    if j == len(buter):
        print('Готовьте бутерброд!')
elif cook_list == biff:
    j = 0
    while j < len(cook_list):
        if cook_list[j] in biff:
            j = j + 1
elif cook_list == ham:
    j = 0
if cook_list == biff:
    print('Вы можете приготовить бифштекс!')
elif cook_list == ham:
    print('Вы можете приготовить гамбургер!')
elif cook_list == ch_ham:
    print('Вы можете приготовить чизбургер!')

