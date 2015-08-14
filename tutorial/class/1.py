class Worker:                               #
    def __init__(self,name,pay):            #
        self.name = name                    #
        self.pay = pay
    def lastname(self):
        return self.name.split()[-1]        #
    def giveRaise(self, percent):
        self.pay *=(1.0+ percent)           #
bob = Worker('Bob Smith', 50000)            #
sue = Worker('Sue Jones', 60000)            #
print(bob.lastname())                       #
print(sue.lastname())                       #
sue.giveRaise(0.1)                          #
print(sue.pay)
