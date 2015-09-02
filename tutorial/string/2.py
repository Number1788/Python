import re                                                               #Импортируем библиотеку для работы со строками
match1 = re.match('Hello[ \t]*(.*)world','Hello    Python world')       #Ищется любая строка,которая начинает с Hello, далее любое количестов табуляции или пробелов[ \t] затем любые произвольные символы
print(match1.group(1))                                                  #котрые будут сохранены как группа совпадения и завершающаяся словом world
mantra = """Always look                                                 
on the bright
side of life"""
print(mantra)                                                           #Многострочная строка
print(len('abc'))                                                       #Длина: число элементов
print('abc' + 'def')                                                    #Конкатенция: новая строка
print('N1!' *4)                                                         #Повторение: Подобно "N1!" + "N1!"+...
print('-' * 80)
myjob = "hacker"
for c in myjob:print(c,end=' ')                                         #Обход элемнетов строки в цикле
print('k' in myjob)                                                     #Поиск подстроки, позиция не возвращается
print('z' in myjob)
print('spam' in 'abscspamdef')
S='spam'
print(S[0],S[-2])                                                       #Индексация
print(S[1:3],S[1:],S[:-1])                                              #Смещение



