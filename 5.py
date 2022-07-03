def my_func():
    while True:
        data = (int(input('Введите число: '))).split()
        for el in data:
            if el == 'stop':
                return
            else:
                print(el)
                sum(data)

print(my_func())