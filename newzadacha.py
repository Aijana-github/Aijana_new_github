list1 = [1,2,3,4,5,6]
def change_list(mode,number):
    if mode == 'add':
        list1.append(number)
    elif mode == 'remove' and number in list1:
        list1.remove(number)
    else:
        print('Вы ввели неверный код!')

change_list('add',7)
change_list('remove',7)
print(list1)



