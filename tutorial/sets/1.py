X = set('spam')                     # Множество из последовательности
Y = {'h','a','m'}                   #МНожество литералами
print(X,Y)                  
print(X & Y)                        #Пересечение
print(X|Y)                          #Объеденение
print(X-Y)                          #Разность
print({x**2 for x in[1,2,3,4]})     #Генератор множеств
x = set('abcde')
y = set('bdxyz')
print('e' in x)                     #Проверка на вхождение в множество
print(x-y)                          #Разность
print(x|y)                          #Объденение
print(x&y)                          #Пересечение
print(x^y)                          #Симетрическая рахность(XOR)
print(x>y,x<y)                      #Надмножество, подмножество
z = x.intersection(y)               #Пересечение 
print(z)
z.add('SPAM')                       #Добавление нового элемента
print(z)
z.update(set(['d','y']))            #Объеденение(?)
print(z)
z.remove('d')                       #Удаление элемента
print(z)
S= set([1,2,3])
print(S.union([3,4]))               #объеденение
print(S.issubset(range(-5,0)))      #проверка является ли S подножеством определнного диапозона
print(S &{1,5})                     #Пересечение литералы
print({1,5} | S)                    #Объеденение
print(S - {1,3})                    #Разность
print(S >{1,3})                     #Надмоножество
s1 = set()                          #Инициализация пустого множества
print(s1)
s1.add(1.23)
print(s1)
print({x for x in 'spam'})          #То же что и set('spam')
print({c * 4 for c in 'spam'})
print({c * 4 for c in 'spamgam'})
L={c * 4 for c in 'spamgam'}
print(L |{'mmmm','xxxx'})
print(L & {'mmmm','xxxx'})
L=[1,2,1,3,2,4,5]
print(L)
L=list(set(L))                      #Удаление повторяющихся значений
print(L)
engineers = {'bob','sue','ann','vic'}
manger =  {'tom','sue'}
print('bob' in engineers)           #боб - инженер?
print(engineers & manger)           #Кто является и инженером и менеджерос
print(engineers | manger)           #Все сотрудник из 2 категорий
print(engineers - manger)           #Инженеры не являющиеся менеджерами
print(manger -engineers)            #Менеджеры не яявляющиеся инженерами
print(engineers > manger)           #Все менеджеры инженеры?(надмножество)
print({'bob','sue'} < engineers)    #Оба сотрудника инженеры?(подмножества)
print((engineers | manger)> manger) #Мнжество все содтрудников является надмножеством менеджеров?
print(engineers ^ manger)           #Сотрудники принадлежавшие в какой-то категори
print ((engineers | manger)         #Пересечение
       - (engineers ^ manger))
