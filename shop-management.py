class Product:
     def __init__(self,name,price,quantity):
            self.product_name = name
            self.product_price = price
            self.product_quantity = quantity

class Store:
        def __init__(self):
            self._product_price ={}
            self._product_quantity ={}

        def add_product(self,name,price,quantity):
            product = Product(name,price,quantity)
            self._product_price [product.product_name] = product.product_name
            self._product_quantity[product.product_name] = product.product_quantity

    
class Shop(Store):
        def __init__(self,name):
            self.shop_name = name
            super().__init__()

shop1 = Shop('my store')

shop1.add_product('Alu',200,'3kg')
shop1.add_product('Piyaj',500,'2kg')
shop1.add_product('roshun',100,'5kg')
print(shop1.product_quantity)  
