a = int(input('введите число, больше 999: '))
if a < 1000:
    print('ошибка! введите число, больше 999!')
elif a >= 1000:
    b = (a // 1000) % 1000
    print('количество тысяч:', b)