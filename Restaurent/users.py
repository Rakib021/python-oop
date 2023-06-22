from abc import ABC ,abstractmethod
class User(ABC):
    def __init__(self,name,email,phone,age):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age


class Customer(User):
    def __init__(self,name,email,phone,age,money):
        self.wallet = money
        self.__order =None
        super().__init__(name,email,phone,age)
    @property 
    def order(self):
        return self.__order
    
    def order(self,order):
        self.__order = order
    