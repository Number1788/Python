#p 192
import math
a=2*(3+4)               #1
b=2*3+4                 #2
c=2+3*4                 #3
print(a,b,c)
a=math.sqrt(4)          #4
b=4**0.5
c=4**2
d=math.pow(4,2)
e=pow(4,0.5)
print(a,b,c,d,e)
a=1+2.0+3               #5Float
print(a)
a=3.14                  #6
b=math.floor(a)
c=math.trunc(a)
d=int(a)
e=round(a)
print(a,b,c,d,e)
a=3                     #7
b=float(a)
c=a/1
d=a+0.0
print(a,b,c,d)
a=2                     #8
b=bin(a)
c=oct(a)
d=hex(a)
print(a,b,c,d)
b=int(b,2)              #9
c=eval(c)
print(b,c)
