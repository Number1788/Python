#игра кости
#импортируем модуль
import random
#создаем случайные числа от 1 до 6
die1 = random.randint(1,6)
die2 = random.randrange(6)+1
total = die1 + die2
print("При вашем броске выпало", die1, "и" , die2, "очков, в сумме", total)
input("\n\n Нажмите Enter, чтоб выйти.")
