a = int(input('Результат пробежки в первый день: '))
b = int(input('Требуемый результат: '))
i = 1
while a < b:
    a = a*1.1
    i += 1
print(i)