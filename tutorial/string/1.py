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
      
