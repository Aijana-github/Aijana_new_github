text = "Miguel is best dancer in this group."


check = text.find('Miguel')
if check > 0:
    print('Он там есть!')
elif check < 0:
    print('Тебя нет в списке!')