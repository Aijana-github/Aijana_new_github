time = int (input())
breafast = False
lunch = False
dinner = False
if 0<=time<24:
    if 8<=time<12:
        breakfast = True
        print(f'Завтрак! {breakfast}',lunch,dinner)
    elif 12<=time<16:
        breakfast = True
        lunch = True

        print(f'Обед!{lunch}',breakfast,dinner)
    elif 16<=time<22:
        breakfast = True
        lunch = True
        dinner = True
        print(f'Ужин!{dinner}',lunch,breakfast)
    else:
        print('Мы не работаем!')
else:
    print('Вы с другой планеты?')