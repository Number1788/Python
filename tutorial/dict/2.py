D = {'a':1,'b': 2, 'c':3}
print(D)
Ks = list(D.keys())                     #Неупорядоченный список ключей
print(Ks)
Ks.sort()                               #Сортировка списка ключей
print(Ks)
for key in Ks:                          #Обход отсортированного списка ключей
    print(key, '=>', D[key])
    
for key in sorted(D):
    print(key, '=>', D[key])            #Сортировка в новой версии
