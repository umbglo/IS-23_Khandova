n = input('введите целое положительное число: ')

while type(n) != int: #обработка исключений
    try:                #соблюдение положительности первого числа
        n = int(n)
    except ValueError:
        print('введите целое число!')
        n = input('введите первое число: ')
    while n < 0:
        try:
            n = abs(n)
        except TypeError:
            print('неправильный ввод, попробуйте еще!')
            n = input('введите первое число: ')
    else:
        n == n
        
k = 1
while k ** 2 < n:
    k += 1
    
print('наибольшее целое число, квадрат которого не превосходит', n, ': ', k-1)
