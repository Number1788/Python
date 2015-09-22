line = 'aaa,bbb,ccc,ddd'
print(line.split(','))      #разделяет строку по разделителю ,
S='spam'
print(S.upper())            #переводит строку в вверхний регистр   
line = 'aaa,bbb,ccc,ddd\n'
print(line.rsplit())        #удаляет заверщающие пробельные символы
print('{0},eggs,and {1}'.format('spam','SPAM'))  #форматирование
help(S.replace)             #получаем полную иннформацию о методе
print(dir(S))               #получаем список всех методов доступных данному объекту
print('A\nB\tC')            #\n конец строки \t табуляция
print(ord('\n'))            #порядковый номер символа
msg=""" aaaaaa
bbbbbb'''bbbbbbb""bbbbb'bbb
ccccccccccccc"""            #"""- многострочная строка-"""
print(msg)
exclamation = "Ni"
print("The knights who say %s!" % exclamation)
print("%d %s %d you" % (1,'spam' , 4))
print("%s -- %s -- %s" % (42,3.14159,[1,2,3]))
x=1234                                          #%d просто целое число
res ="integers:...%d...%-6d...%06d" % (x,x,x)   #%-6d число выравненое по левому краю с 6 символоми(тк символов нет там пробелы)
print(res)                                      #%06d число с ведущими нулями и 6 символами
x= 1.23456789
print(x)
print('%e|%f|%g' %(x,x,x))                      #различные варианты написания чисел
print('%E' % x)
print('%-6.2f|%05.2f|%+06.1f' %(x,x,x))         #-6.2f выравнивание по левому 6 символов 2
print("%s" %x, str(x))
print('%f,%.2f,%.*f' %(1/3.0, 1/3.0,4,1/3.0))
print('%(n)d %(x)s' % {'n':1,'x':'spam'})       #форматирование со словарем
reply ='''
Greerings...
Hello %(name)s!
You age squared is %(age)s
'''                                             #Шаблон с замещаемым специфакотором формата
values = {'name':'Bob', 'age':40}               #подготовка фактических значений
print(reply % values)                           #Подстановка значений
food ='spam'
age=40
z=vars()                                        #функция собирающая все переменные в словарь
print(z)
print("%(age)d %(food)s" %z)
template = '{0}, {1} and {2}'                   #порядковые номера позиционных аргументов
print(template.format('spam','ham','eggs'))
template = '{notto}, {pork} and {food}'         #Имена именнованых аргументов
print(template.format(notto='spam', pork ='ham', food ='eggs'))
template = '{notto}, {0} and {food}'             #оба варианта
print(template.format('ham', notto= 'spam', food = 'eggs'))
print('{motto}, {0} and {food}'.format(42, motto=3.14, food = [1,2]))
X='{motto}, {0} and {food}'.format(42, motto=3.14, food = [1,2])
print(X)
print(X.split(' and '))
Y= X.replace('and', 'but under no circumatances')
print(Y)
import sys
print('My {1[spam]} runs {0.platform}'.format(sys,{'spam':'laptop'}))
                                                #Позиционные аргументы
print('My {config[spam]} runs {sys.platform}'.format(sys=sys,config={'spam':'laptop'}))
                                                #Именные аргументы
somelist= list('Spam')
print(somelist)
print('first = {0[0]}, last ={0[2]}'.format(somelist))
print('{0:10} = {1:10}'.format('spam', 123.4567))
print('{0:>10} = {1:>10}'.format('spam', 123.4567)) #выравнивание по правому краю
print('{0:<10} = {1:<10}'.format('spam', 123.4567)) #выравнивание по левому краю
print('{0:e},{1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159)) #представления чисел с помощью формата
print('{0:f},{1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))
print('{0:x},{1:o}, {2:b}'.format(255,255,255)) #Шестнадцетиричное, восьмеричное и двоичное представление
print('{0:.2f}'.format(1/3.0))                  #парметры определенны непосредственно в строке формата
print('%.2f' % (1/3.0))
print('{0:.{1}f}'.format(1/3.0,4))              #Значение извлекаются из списка аргументов
print('%.*f' % (4, 1/3.0))
