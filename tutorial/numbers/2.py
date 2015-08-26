from fractions import Fraction              #Библиотека рациональных чисел
x= Fraction(1,3)                            #числитель знаминатель
y = Fraction(4,6)                           #округляется до 2/3
print(x,y)
print(x+y)                                  #сложение
print(x-y)                                  #вычитание
print(x*y)                                  #умножение
print(Fraction('.25'))                      #преобразуем вещественные числа в рациональные
print(Fraction('1.25'))
print(Fraction('.25')+Fraction('1.25'))
print((2.5).as_integer_ratio())             #Получение числителя и знаменателя
f = 2.5
z = Fraction(*f.as_integer_ratio())         #Преобразуем float -> fraction
print(z)
print(x)
print(x+z)
print(float(x))                             #Перобразуем fraction -> float
print(float(z))
print(Fraction.from_float(1.75))            #Преобразуем float -> fraction
print(Fraction(*(1.75).as_integer_ratio ()))
print(x*2)                                  #Fraction * int -> fraction
print(x*2.0)                                #Fraction * float - > float
print(x*1./3)                               #Fraction * float - > float
print(x*4./3)                               
print(x*Fraction(4,3) )                     #Fraction * Fraction - > float
print(4.0/3)
print((4.0/3).as_integer_ratio() )          #Произойдет потеря точности
a = x * Fraction(*(4.0/3).as_integer_ratio())
print(a)
print(2001599834386887/4503599627370496)    
a=a.limit_denominator(10)                   #упростить до ближайшего рационального
print(a)
