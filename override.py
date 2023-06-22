class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print("vath khailam")

class Cricketer(Person):
    def __init__(self,name,age,height,weight,team):
        self.team = team

        super().__init__(name,age,height,weight)
#override
    def eat(self):
        print('pizza khailam')
        #dander mathod
    def __add__(self,other):
        return self.age + other.age
    def __mul__(self,other):
        return self.height * other.height
      

sakib= Cricketer('sakib',33,67,76,'BD')
mushi = Cricketer('mushi',54,65,43,'bd')

print(sakib + mushi)
print(sakib * mushi)
sakib.eat()
