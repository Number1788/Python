# пирожок
import random
value = random.randrange(5)
print(value)
if value == 0:
    print("Vse ploho")
elif value == 1:
    print("skoro vse naladitsa")
elif value == 2:
    print("u vas vse normalno")
elif value == 3:
    print("u vas vse horosho")
else:
    print("vam povezlo")
input("Press Enter to exit")
#орел или решка
count = 0
coins = 0
head = 0
tail = 0
while count < 100:
    coins = random.randrange(2)
    if coins == 0:
        head += 1
    else:
        tail += 1
    count += 1
print("Kolichestvo orlov - ", head, ", kolichestvo reshek - ", tail)
input("Press Enter to exit")
# угадай число с количеством попыток
attempt = 10
number= random.randint(1,100)
while attempt > 0:
    user_number= int(input("Vvedite chislo - "))
    attempt -=1
    if user_number == number:
        break
    elif user_number > number:
        print("Vashe chislo bolshe")
    else:
        print("Vashe chislo menshe")
if attempt > 0 :
    print("Vi ugadali chislo - ",number ," s ", 10-attempt," popitki")
else:
    print("Vi ne ugadali chislo - ",number)
input("Press Enter to exit")
# отгадывает компьютер
number_user=int(input("Vvedite chislo  ot 1 do 100 - "))
minimum=1
maximum=100
tr=0
while True:
    number_pc=(maximum+minimum)//2
    tr += 1
    print("Comp ugadivaet, ego otvet - ", number_pc)
    if number_pc == number_user:
        break
    elif number_pc > number_user:
        print("Nepravilno davai eshe")
        maximum =number_pc
    else:
        print("Nepravilno davai eshe")
        minimum= number_pc
print("Eto pravilno! kolichestvo popitok - ", tr)
