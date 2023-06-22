class User:
    def __init__(self,name,age,money):
        self._name = name
        self._age = age
        self.__money = money

    @property
    def salary(self):
        return self.__money

samsu = User('samsu',21,1200)

# print(samsu._age)
print(samsu.salary)