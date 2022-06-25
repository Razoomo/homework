my_list = list(input('Введите элементы списка: '))
i = 0
while i < my_list.count()
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i += 1
print(my_list)