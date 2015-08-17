class Worker:                               #Описание класса
    def __init__(self,name,pay):            #Инцилизация при созднаии
        self.name = name                    #self  -это сам объект
        self.pay = pay
    def lastname(self):
        return self.name.split()[-1]        #Разбить строку по символам
    def giveRaise(self, percent):
        self.pay *=(1.0+ percent)           #Обновить сумму выплат
bob = Worker('Bob Smith', 50000)            #Создается 2 экземпляра и для каждого
sue = Worker('Sue Jones', 60000)            #определяется имя и сумма выплат
print(bob.lastname())                       #Вызов метода self - это bob
print(sue.lastname())                       #self - это sue
sue.giveRaise(0.1)                          #обновить сумму выплат для sue
print(sue.pay)
