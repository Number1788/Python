L=[123,'123',1.23]
print(len(L))                           #Длина строки
print(L[0])                             #Возвращаем элемент по индексу
print(L[:1])                            # делаем срез до второго элемента
print(L + [4,5,6])                      # контатация сторк
print(L)
print(len([1,2,3]))                     #длина
print([1,2,3] + [4,5,6])                #конктенация
print(['Ni!'] * 4)                      #повторение
print(3 in [1,2,3])                     #Проверка  на вхождение
for x in [1,2,3]:
    print(x,end=' ')                    #Итерации
res = [c * 4 for c in 'SPAM']           #генератор списка
print(res)
res = []
for c in 'SPAM':
    res.append(c * 4)                   #эквивалент генератор списка
print(res)
print(list(map(abs, [-1,-2,0,1,2])))    #Функция map применяется последованости
L= ['spam','Spam','SPAM!']
print(L[2])                             #Отчет смещений начинается с нуля
print(L[-2])                            #Отрицательное смещение: отчитывается справа
print(L[1:])                            #Операция извлечения среза возвращает разделы списка
matrix =[[1,2,3],[4,5,6],[7,8,9]]       #Работа с многомерным массивом
print(matrix[1])
print(matrix[2][0])
print(matrix)
print(matrix[1][1])
L = ['spam','Spam', 'SPAM!']
L[1]= 'eggs'                            #Присваивание по индексу элементу
print(L)
L[0:2] = ['eat','more']                 #ПРисваивание срезу:удаление + вставка
print(L)                                
L.append('please')                      #Вызов метода добавление элемента в конец списка
print(L)
L.sort()                                #Сортировка элементов списка (S<e)
print(L)
L=['abc','ABD','aBe']
L.sort()
print(L)
L.sort(key=str.lower)                   #Приведение символов к нижнему регистру
print(L)
L.sort(key=str.lower,reverse =True)     #изменяет напрваление сортировки
print(L)
L = sorted(L, key = str.lower, reverse = True)      #Встроенная функция сортировки
print(L)
L = sorted([x.lower() for x in L], reverse = True)  #Элементы изменяются предварительно
print(L)
L=[1,2]
L.extend([3,4,5])                       #Добавление несколько элементов в конец
print(L)
print(L.pop())                          #Удаляет и возвращает послдедний элемент из списка
print(L)
L.reverse()                             #Изменяет порядок следования на обратный
print(L)
L=list(reversed(L))                     #Встроенная функция сортировки в обратном порядке
print(L)
#Реализация стека-последний пришел, первый ушел(LIFO)
L=[]
L.append(1)                             #Втолкнуть на стек
L.append(2)
print(L)
L.pop()                                 #Вытолкнуть со стека
print(L)
#---end---
L = ['spam', 'eggs', 'ham']
print(L.index('eggs'))                  #Индекс объекта
L.insert(1,'toast')                     #Вставка в требуемую позицию
print(L)
L.remove('eggs')                        #Удаление элемента с определнныи значением
print(L)
print(L.pop(1))                         #Удаление элемента в указанной позиции
print(L)
