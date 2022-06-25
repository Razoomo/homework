my_str = input('Введите строку: ')
li = []
num = 1
for el in range(my_str.count(' ') + 1):
    li = my_str.split()
    if len(str(li)) >= 10:
        print(f"{num} {li[el]}")
        num += 1
    else:
        print(f" {num} {li [el] [0:10]}")
        num += 1