class ItemInfo:

     def __init__(self,item_code,item,price,qty,discount,net_price):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price

     def calculate_discount( self):

        if self.qty<=10:
           self.discount=0
           self.message="discount is 0 "
        elif self.qty>11 and self.qty<20:
             self.discount=15
             self.message="discount is 15 "
        elif self.qty >= 20:
            self.discount=20
            self.message="discount is 20"

        """self.net_price = self.price * self.qty - self.discount"""

        return self.message



     def buy(self,):
         self.item_code=int(input("item_code için bir değer giriniz:",))
         self.item=int(input("item için bir değer giriniz:",))
         self.price = int(input("price için bir değer giriniz:",))
         self.qty = int(input("qty için bir değer giriniz:",))

         self.net_price = self.price * self.qty - self.discount

         return "net_price:" ,self.net_price


     def show_all(self):
         print("item_code:",self.item_code ,"item:",self.item,"price:",self.price,"discount:",self.discount,"qty:",self.qty,"net_price:",self.net_price)



x=ItemInfo(0,10,5,4,6,7)

print(x.buy())
print(x.calculate_discount())
print(x.show_all())






