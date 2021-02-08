'''
Define a class named ItemInfo with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), 
discount(Discount percentage on the item), net_price(Price after discount)
Methods :
A member method calculate_discount() to calculate discount as per the following rules:
If qty <= 10 —> discount is 0
If qty (11 to 20 inclusive) —> discount is 15
If qty >= 20 —> discount is 20
A constructor init method to assign the initial values for item_code to 0 and price, qty, 
net_price and discount to null
A function called buy() to allow user to enter values for item_code, item, price, qty. 
Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
A function show_all() or similar name to allow user to view the content of all the data members.
Author= Bulent Caliskan  date= 08/02/2021
'''
class ItemInfo:
    def __init__(self,item_code,item,price,qty,discount,net_price):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price
    
    def calculate_discount(self):
        if self.qty<=10:     return 0
        elif 11<self.qty<20: return 15
        else:                return 20

    def buy(self):
        try:
            self.item_code = int(input("Enter code of item ? "))
            self.item = input("Enter name of item ? ")
            self.price = int(input("Enter price of each item ? "))
            self.qty = int(input("Enter quantity in stock ? "))  
            self.net_price=(self.price*self.qty)- ItemInfo.calculate_discount(self) 
        except:print("Please enter the value you entered correctly. ")     
    
    def show_all(self):
        print(f"Item Code         : {self.item_code}\
                  \nItem name         : {self.item}\nItem price        : {self.price}\
                       \nQuantity in stock : {self.qty}\nNet Price          : {self.net_price} ")    


item1= ItemInfo(0,0,0,0,0,0)
item2= ItemInfo(0,0,0,0,0,0)

item1.buy()
item1.show_all()

item2.buy()
item2.show_all()



        