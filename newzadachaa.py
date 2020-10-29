def millionaire():
    answer_list = ['Шекспир', 'Пушкин', 'Бунин', 'Булгаков']
    true_answer = 'Булгаков'
    print("Ответьте на вопрос: Кто написал Мастер и Маргарита?")
    print('Варианты ответов:',answer_list)
    help = input("Нужны ли вам подсказки?")
    if help == 'да':
        poll = input("У вас три подсказки: 50x50, звонок другу,помощь зала")
        if poll == '5050':
            for i in range(2):
                if answer_list[i] != true_answer:
                    answer_list.remove(answer_list[i])
            print(answer_list)
            my_answer = input('Введите свой ответ:')
            if my_answer == true_answer:
                return 'Вы победили забирайте деньги!'
            else:
                return 'Вы ответили неверно! Вылетаете'
        elif poll == 'помощь зала':
            help_list = []
            for i in range(6):
                help_answer = input("Введите ответ с зала: ")
                help_list.append(help_answer)
            print(help_list)
            if my_answer == true_answer:
                return 'Вы победили забирайте деньги!'
            else:
                return 'Вы ответили неверно! Вылетаете'
        elif poll == 'звонок другу:':
            call_answer = input("Введите ответ на вопрос: ")
            print(call_answer)
            my_answer = input('Введите свой ответ:')
            if my_answer == true_answer:
                return 'Вы победили забирайте деньги!'
            else:
                return 'Вы ответили неверно! Вылетаете'
        elif help == 'нет':
            my_answer = input('Введите свой ответ:')
            if my_answer == true_answer:
                return 'Вы победили забирайте деньги!'
            else:
                return 'Вы ответили неверно! Вылетаете'
        else:
            print('Введите да или нет')

print(millionaire())