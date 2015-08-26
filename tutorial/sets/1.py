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
z.update(set(['dx','y']))           #Объеденение
print(z)
z.remove('dx')                      #Удаление элемента
print(z)
