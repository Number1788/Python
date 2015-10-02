D= {'food': 'Spam', 'quantity': 4, 'color':'pink'}      #Инициализируем словарь
print(D['food'])                                        #Выводим значение с ключом food
D['quantity'] +=1                                       #Добавить +1 к значению ключа quantity
print(D)    
F={}                                                    #Другой способ создания словаря
F['name']= 'Bob'
F['job']='dev'
F['age']=40
print(F)
print(F['name'])            
rec = { 'name' : {'first': 'Bob', 'last':'Smith'},      #Создаем вложенный словарь
        'job': ['dev','mgr'],
        'age':40.5
    }
print(rec['name'])                                      #ОБращение к вложенному словарю
print(rec['name']['last'])                              #Обращение к элементу словаря по ключу
print(rec['job'])
print(rec['job'][-1])                                   #Обращение к элементу словаря по индексу
D={'spam':2,'ham':1, 'eggs':3}                          #Создание словаря
print(D['spam'])                                        #извлечение по ключу
print(D)                                                #случайный порядок следования
print(len(D))                                           #число элементов словаря
print('ham' in D)                                       #Проверка на вхождение
print(list(D.keys()))                                   #создает новый список ключей
D['ham'] = ['grill', 'bake','fry']                      #Изменение элемента
print(D)
del D['eggs']                                           #Удаление элемента
print(D)
D['brunch']='Bacon'                                     #Добавление новго элемента
print(D)
print(D['ham'])
D={'spam':2, 'ham':1,'eggs':3}
print(list(D.values()))
print(list(D.items()))
print(D.get('spam'))                                    #Ключ присутсвтует в словаре
print(D.get('toast'))                                   #Ключ отсутствует
print(D.get('toast',88))                                #Ключ оствует, 88 значенеие по умолчанию
