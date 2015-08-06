for c in 'spam':            #цикл for
    print(c.upper())
x=4
while x >0:                 #цикл while
    print('spam!' * x)
    x-=1
squares = [x ** 2 for x in [1,2,3,4,5]]     #вычисление в списке, x**2 возведение в степень
print(squares)
squares = []
for x in [1,2,3,4,5]:                       #тоже вычисление, но механизмом итераций
    squares.append(x**2)
print (squares)
