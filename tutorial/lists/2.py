L=[123,'spam',1.23]     #Иницилизация массива
L.append('Ny')          #Добавление нового элемента
L.pop(2)                #Удаление элемента по индексу
print(L)
del L[2]                #Удаление  элемента по индексу
print (L)       
L.insert(2,123)         #вcтавка элемента в произвольное место
print(L)
L.remove(123)           #удаляет первый попавшийся элемент по названию       
print(L)
M = ['bb','aa','cc']
M.sort()                #Сортировка по возрастанию
print (M)
M.reverse()             #Сортировка по убыванию
print(M)                
N = [[1,2,3],           #Вложенный список
     [4,5,6],           #Выражение в [] может занимать несколько строк
     [7,8,9]]
print(N)
print(N[1])             #Получаем строку 2
print(N[1][2])          #Из 2 строки получаем 3 элемент
col2=[row[1] for row in N]  #получаем 2 столбец
print(col2)
print(N)
col=[row[1]+1 for row in N] #Добавить 1 к каждому элементу во втором столбце
print (col)
col1=[row[1] for row in N if row[1] % 2==0] #отфильтровать нечетные значения во 2 столбце
print(col1)
diag = [N[i][i] for i in [0,1,2]]   #Выборка диогонали матрицы
print(diag)
doubles = [c * 2 for c in 'spam']   #Дублирование символов в строке с-обозначает символ
print(doubles)
G=(sum(row) for row in N)   #возращает сумму элементов строк
print(next (G))             # 1 строка
print(next (G))             # 2 строка
print(list(map(sum,N)))     # с помощью map оборачиваем все сразу и выводи все суммы
print({sum(row) for row in N})  #Создает множество сум строк
print({i:sum(N[i]) for i in range(3)})  #Таблица ключ/значение сумм строк
print([ord(x) for x in 'spaam'])  # Список кодов символов
print({ord(x) for x in 'spaam'})    #Множества убирают дубликаты
print({x:ord(x) for x in 'spaam'})  #Ключи словарей являются уникальными
P=[1,2,4]
O=P[:]                              #Копирование элемента
P[0]=24
print(P,O)

