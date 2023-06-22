class Shopping:
    cart =[] #class attribute #static attribute

    def __init__(self,name,location):
        self.name = name #instance attribute
        self.location = location

    @classmethod
    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f'buying :{item} for price: {price} and remaining : {remaining}')

bashundhara = Shopping("bashundhara" ,"not a popular location")
bashundhara.purchase(2,43,54)

Shopping.purchase(2,65,12)
