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
print(D)
D2={'toast':4, 'muffin':5}
D.update(D2)
print(D)
#удаление элемента словаря по ключу
print(D.pop('muffin'))
print(D.pop('toast'))                                   #Удаляет и возвращает значение заданного ключа
table = {'Python': 'Guido van Rossum',
         'Perl': 'Lary Wall',
         'Tol': 'John Ousterhout'}
language = 'Python'
creator = table[language]
print(creator)
for lang in table:                                      #То же что и  for lang in table.keys()
    print(lang, '\t', table[lang])
Matrix = {}
Matrix[(2,3,4)]=88
Matrix[(5,6,7)]=99
x=2;y=3;z=4
print(Matrix)
rec={}                                                  #структуированный список
rec['name']='mel'
rec['age']=45
rec['job']='trainer\writter'
print(rec['name'])
mel={ 'name':'Mark',
      'jobs':['trainer','writter'],
      'web':'www.rmi.net/"lutz',
      'home':{'state':'Co','zip':80153}}                #другой вид структурированного списка
print(mel['name'])
print(mel['jobs'])
print(mel['jobs'][1])
print(mel['home']['zip'])
{'name':'mel','age':45}                                 #Традиционноелитеральное выражение
D={}                                                    #Динамическое присваивание по ключам
D['name']='male'
D['age']=45
dict(name='mel',age=45)                                 #форма именновых аргументов
dict([('name','male'),('age',45)])                      #Кортежи ключ\ значение
list(zip(['a','b','c'],[1,2,3]))                        #объеденить ключи и значения
D=dict(zip(['a','b','c'],[1,2,3]))                      #Создать словарь из результов
print(D)
D={k:v for (k,v) in zip(['a','b','c'],[1,2,3])}         #генераторы словарей
print(D)
D={x:x ** 2 for x in range(1,5)}
print(D)
D={c: c * 4 for c in 'SPAM'}                              #цикл через итерируемый объект
print(D)
D= {c.lower(): c + '!' for c in ['SPAM','EGGS','HAM']}
print(D)
