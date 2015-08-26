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
s1 = set()
print(s1)
s1.add(1.23)
print(s1)

