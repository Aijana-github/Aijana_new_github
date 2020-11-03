def settiffy(number_list):
    number_list.sort()
    empty_list = []
    for number in number_list:
        empty_list.append(number)
    return empty_list


print(settify([1,2,3,3,4,4,5,5,6,6]))