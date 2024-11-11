class Flower:
    def __init__(self,fname,fprice,fstock):
        self.__name=fname
        self.__price=fprice
        self.__stock=fstock

    def get_flowername(self):
        return self.__name
    def get_flowerprice(self):
        return self.__price
    def get_flowerstock(self):
        return self.__stock

    def set_flowername(self,newname):
        self.__name=newname
    def set_stock(self,newstock):
        self.__stock=newstock

    def validate_name(self,name):
        if self.__name==name:
            return True
        else:
            return False
    def validate_stock(self,stock):
        if stock<=self.__stock:
            return True
        else:
            return False

    def sell_flower(self,name,stock):
        if self.__name==name and self.__stock>=stock:
            self.__stock-=stock
            return self.__stock
        else:
            return "Stock is not available"
    def check_level(self,level):
        if self.__stock>=level:
            return "Stock is available for order"
        else:
            return "Stock is not available for order"

f1=Flower("Orchid",100,35)
f2=Flower("Jasmine",120,25)
f3=Flower("Rose",90,40)
print("Flower Name:",f1.get_flowername())
print("Flower Price:",f1.get_flowerprice())
print("Flower Stock:",f1.get_flowerstock())
print("Available stock:",f1.sell_flower("Orchid",10))

print("Flower Name:",f2.get_flowername())
print("Flower Price:",f2.get_flowerprice())
print("Flower Stock:",f2.get_flowerstock())
