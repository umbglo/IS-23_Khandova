#Из списка ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
#получить новый список в котором длина слов не превышает 5 символов.

names = ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']

n5s = [] #пустой список

for names[0] in names:
    if len(names[0]) <= 5: #ограничение по длине
        n5s.append(names[0]) #добавление элемента в список, если он соблюдает условие

print(n5s) #вывод результата
