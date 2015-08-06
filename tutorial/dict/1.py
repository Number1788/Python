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
