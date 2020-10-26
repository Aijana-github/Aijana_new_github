import random
file1 = open('players.txt','w')
for i in range(6):
    player = input("Введите имя нового игрока за столом: ")
    file1.write(player+'\n')
file1.close()
file2 = open('players.txt')
players_list = file2.readlines()
cards = []
for i in range(6):
    cost = random.randint(2,11) + random.randint(2,11)
    check = input(f"Ваша рука: {cost} Нужна еще карта? Да или нет")
    if check == 'Да':
        cost = cost + random.randint(2,11)
    elif check == 'Нет':
        cost = cost
    else:
        print('Ответьте точно Да или Нет')
    cards.append(cost)
print(cards)
i = 0
while i < len(cards):
    if cards[i] > 21:
        cards[i] = 0
    i = i +1
max_cost = max(cards)
second_max = -1

for number in cards:
    if number == max_cost and cards.index(max)

i = 0
while i < len(cards):
    if cards[i] > 21:
        cards[i] = 0
    i = i + 1
max_cost = max(cards)
max_index = cards.index(max_cost)
winner = players_list[max_index]
print(f'ВСТРЕЧАЙТЕ ПОБНДИТЕЛЯ! {winner}')