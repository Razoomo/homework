arg_1 = int(input("Введите Делитель "))
arg_2 = int(input("Введите Делитель "))
def my_func(arg_1, arg_2):
    try:
        res = arg_1 / arg_2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return res

print(my_func(arg_1, arg_2))