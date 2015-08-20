print(1/3)                                          #Обычное деление
print((2/3)+(1/2))
import decimal                                      #Импортируем библиотеку чисел с плавающей запятой
d=decimal.Decimal('3.141')
print(d+1)
decimal.getcontext().prec=2                         #Установкак количества знаков после заптяой
print(decimal.Decimal('1')/decimal.Decimal('3'))
from fractions import Fraction                      #Рациональные числа:числитель + знаменатель
f= Fraction(2,3)
print(f+1)
print(f +Fraction(1,3))
X=1
Y=2
Z=4
print((X+Y)*Z)                                      #Меняем старшинство операторов
print(X+(Y*Z))
print(int(3.1415))                                  #Усекаем дробную часть
print(float(3))                                     #Преобразуем цело в вещественное
