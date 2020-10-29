
# Найдите максимум трех чисел с помощью функции
def max_of_four(number1,number2,number3,number4):
    max1 = max(number1,number2)
    max2 = max(number3,number4,number3)
    max3 = (max1,max2)
    print(max3)

max_of_four(10,20,40,50)

    