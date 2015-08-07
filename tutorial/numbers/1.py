print(1/3)                                          #Обычное деление
print((2/3)+(1/2))
import decimal                                      #Импортируем библиотеку чисел с плавающей запятой
d=decimal.Decimal('3.141')
print(d+1)
decimal.getcontext().prec=2                         #Установкак количества знаков после заптяой
print(decimal.Decimal('1')/decimal.Decimal('3'))
