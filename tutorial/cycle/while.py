# Симулятор трехлетнего ребенка
# Демонстрирует работу цикла while
print("\tДoбpo пожаловать в программу 'Симулятор трехлетнего ребенка'\n")
print("Имитируется разговор с маленьким ребенком.")
print("Попробуйте остановить этот кошмар.\n")
response = ''
while response != "Потому что":
    response = input("Почему?\n")
print("А, ладно")
input("\n\nHaжмитe Enter. чтобы выйти.")
# Проигранное сражение
print("Baшeгo героя окружила огромная армия троллей.")
print("Смрадными зелеными трупами врагов устланы все окрестные поля.")
print("Одинокий герой достает меч из ножен . готовясь к последней битве в своей жизни.\n")
health = 10
trolls = 0
damage = 3
while health>0:
    trolls +=1
    health -=damage
    print("Взмахнув мечом. ваш герой истребляет злобного тролля. " \
          "но сам получает повреждений на",  damage, "очков . \n")
print( "Ваш герой доблестно сражался и убил" , trolls, "троллей.")
print("Ho увы! Он пал на поле боя ")
input("\n\nHaжмитe Enter. чтобы выйти ")
#Считалка
#Демонстрирует break и continue
count = 0
while True:
    count +=1
    #завершить цикл, если count принимает значение больше 10
    if count > 10:
        break
    #пропустить 5
    if count == 5:
        continue
    print(count)
input("\n\nНажмите Enter, чтоб выйти")
    