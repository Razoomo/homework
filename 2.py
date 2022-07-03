def my_func(name, surname, year, city, email, telephone):
    print(surname, name, year, city, email, telephone)


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = int(input('Введите год рождения: '))
city = input('Введите город: ')
email = input('Введите email: ')
telephone = input('Введите номер телефона: ')

my_func(surname, name, year, city, email, telephone)