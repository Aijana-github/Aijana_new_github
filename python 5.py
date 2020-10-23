hour_salary = 70
salary = 0
work = int(input("Введите кол-во часов работы: "))

work_day = 8 # Рабочий день

if work > 1 and work <= 24:
    if work > work_day:
         # Кол-во часов переработки
       check = work - work_day
     # зарплата включающуя двойную ставку за переработанное время
     salary = (work_day *hour_salary) + (check * hour_salary*2)
     print(f'Ваша зарплата за сегодня: {salary}')
    else:
     # считаем зарплату
     salary = hour_salary * workprint(f'Ваша зарплата за сегодня: {salary}$')
else:
print('Ты врешь,ничего не получишь!')
