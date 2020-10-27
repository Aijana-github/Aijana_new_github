list1 = [1,2,3,4,5,6]
def change_list(mode,number):
    if mode == 'add':
        list1.append(number)
    elif mode == 'pop' and number in list1:
        list1.pop(number)
    elif mode == 'remove' and number in list1:
        list1.remove(number)
    elif mode == 'pop':
        if number >= len(list1):
            print('Вы ввели сликом большое число')
    else:
        print('Вы ввели неверный мод!')

change_list('add',7)
change_list('pop',5)
change_list('remove',7)
print(list1)