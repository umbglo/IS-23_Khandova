#Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае
#вычесть из него 2. Вывести полученное число.

a = input('введите целое число: ')

while type(a) != int: #обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('вы ввели не целое число!')
        a = input('введите целое число: ')

if a >= 0:
    b = a + 1
    print(a, '+ 1 = ', b)
else:
    b = a - 2
    print(a, '- 2 = ', b)
