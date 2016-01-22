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
S='abcdefghijklmnop'
print(S[1:10:2])                                                        #c первого по десятый срез каждый второй элемент
print(S[::2])                                                           #с начала и до конца каждый второй элемент
S='hello'
print(S[::-1])                                                          #пероварачиваем слово наоборот
S='abcedfq'
print(S[5:1:-1])                                                        #со второго по 5 в обратном порядке
print('spam'[1:3])                                                      #Синтаксис извлечения среза
print('spam'[slice(1,3)])                                               #используется объект среза
print('spam'[::-1])                                                     
print('spam'[slice(None,None,-1)])
print(int("42"),str(42))                                                #преобразование из/в строки
print(repr(42))                                                         #преобразование в строку как если б она была литералом
S='42'
I=1
print(int(S)+I)                                                         #сложение
print(S+str(I))                                                         #конкатенации
print(str(3.1415),float('1.5'))
text="1.234E-10"
print(float(text))
print(ord('s'))                                                         #получение порядкового номера символа
print(chr(115))                                                         #преобразование номера в символ        
S = '5'
S = chr(ord(S)+1)
print(S)
S = chr(ord(S)+1)
print(S)
print(int('5'))                                                         
print(ord('5') - ord('0'))                                              #замена int()
B = '1101'                                                              #Двоичные цифры преобразуются в числа
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]
print (I)
S = 'spam'
S = S + 'SPAM!'                                                         #Чтобы изменить строку, нужно создать новую
print(S)
S = S[:4] + 'Burger' + S[-1]
print(S)
S= 'splot'
S = S.replace('p1', 'pamal')
print(S)
print('That is %d %s bird!' % (1, 'dead'))                              #Выражение форматирования
print('That is {0} {1} bird!'.format(1,'dead'))                         #Методы форматирования
S = 'spammy'
S = S[:3] + 'xx' + S[5:]                                                #замена подстрок стнадратным способом
print(S)
S = 'spammy'
S = S.replace('mm', 'xx')                                               #замена при помощи методов
print(S)
print('aa$bb$cc$dd'.replace('$', 'SPAM'))
S='aaSPAMbbSPAMccSPAMdd'
where = S.find('SPAM')                                                  #Поиск позиции
print(where)
S = S[:where] + 'EGGS' + S[(where + 4):]                                #Замена на основе поиска
print(S)
S='aaSPAMbbSPAMccSPAMdd'
print(S.replace('SPAM', 'EGGS'))                                        #Заменить все найденные подстроки
print(S.replace('SPAM', 'EGGS',1))                                      #Заменить одну подстроку
S = 'spammy'
L = list(S)                                                             #Разбивка неизменяемой строки на изменяемый список
print(L)
L[3] = 'x'                                                              #Этот прием допустим для списка, но не для строк
L[4] = 'x'
print(L)
S= ''.join(L)                                                           #Метод join
print(S)
print('SPAM'.join(['eggs','sausage','ham','toast']))
line = 'aaa bbb ccc'
col1 = line[0:3]                                                        #разбор текста путем срезов
col3 = line[8:]
print(col1)
print(col3)
cols = line.split()                                                     #разбор текста метод 
print(cols)
line = 'bob,hacker,40'
cols=line.split(',')
print(cols)
line = "1'mSPAMaSPAMlumberjack"
cols=line.split("SPAM")
print(cols)
line = "The khignts who say Ni!\n"
print(line.rstrip())                                                    #убираем пробельные символы справа
print(line.upper())                                                     #вверхний регистр
print(line.isalpha())                                                   #прверяем все ли символы алфавитные
print(line.endswith('Ni!\n'))                                           #проверка конца строки   
print(line.startswith('The'))                                           #проверка начала строки
print(line.find('Ni') != -1)                                            #поиск с использованием метода или выражения
print('Ni' in line)
sub = 'Ni!\n'
print(line.endswith(sub))                                               #проверка наличия подстроки в конце строки
print(line[-len(sub):]==sub)                                            #с помощью метода или операции извлечения подстроки
#Только согласные
#Демонстрирует как создавать новые строки из исходных с помощью цикла for
message = input("Vvedite text: ")
new_message = ""
VOWELS="aeiouаеёиоуыэюя"
print()
for letter in message:
    if letter.lower() not  in VOWELS:
        new_message += letter
        print("Sozdana new string: ", new_message)
print("\nVot vash text bez glasnih:", new_message)
input("\n\nPress Enter to exit")
