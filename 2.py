sec = int(input('Введите время в секундах: '))
if sec >= 3600:
    hour = sec//3600
    sec = sec%3600
    if sec >= 60:
        minute = sec//60
        sec = sec%60
    elif sec < 60:
        minute = 0
elif sec < 3600 and sec >=60:
    hour = 0
    minute = sec//60
    sec = sec%60
print(f'Время: {hour}:{minute}:{sec}')
