'''
Write a Customer class and Items class. Let user enter customer information and add stuff to his/her
 shopping card.
Class Items :
Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()
calculate_discount():
total_price = price * qty
discount —> 25% if total_price >= 4000
discount —> 15% if total_price >= 2000
discount —> 10% if total_price < 2000
price_tobe_paid = total_price – discount
shopping_cart():
Let user add items in the shopping basket. Be creative with the items, set their prices as well.
__str__():
Print items added and total price nicely.
Class Customer :
Methods: __init__(), get_cust_info() this is optional, __str__()
Optionally create a get_cust_info() or similar to allow customer to enter his/her information or 
just define them in __init__() and pass customer information as arguments while creating a customer object.
__str__():
Print customer information and price nicely.
Find a way to link two classes. For example, instances of both classes may have a customer number. 
With a get method, get the customer number and pass it to the item object as an argument to 
set customer number attribute. So Customer class instance holds the customer info, Items class holds 
the shopped item’s info for the same customer ID number such as price, quantity or so.
In the end, print both info (customer info and shopped items info) using their respective __str__ format 
in a nice way.
Simple example:
Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, 
discount : 300, price_tobe_paid : 1700]
Author= Bulent Caliskan  date= 08/02/2021
'''
class Items:

    def __init__(self,item_name,price,qty,total_price,price_tobe_paid):
        self.item_name = item_name
        self.price = price
        self.qty = qty
        self.total_price=total_price
        self.price_tobe_paid = price_tobe_paid
    def shopping_cart(self):
        
        self.item_name=input("Enter item name? ")
        self.price=int(input("Enter price of item? "))
        self.qty=int(input("Enter quantity of item? "))

    def __str__(self):
        print (f"Item name        : {self.item_name}\
                  \n{self.item_name} price     : {self.price}\
                        \nQuantity of item : {self.qty}\
                             \nDiscount         : {Items.calculate_discount(self):.5}\
                                 \nPrice to be paid : {Items.get_total_amount(self)}")
        

    def calculate_discount(self):
        self.total_price = self.price * self.qty
        if self.total_price >= 4000 : return self.total_price*0.25
        elif self.total_price >= 2000 : return self.total_price*0.15
        elif self.total_price < 2000 : return self.total_price*0.10


    
    def get_total_amount(self):
        self.price_tobe_paid=self.total_price-Items.calculate_discount(self)
        return self.price_tobe_paid

        
class Customer:
    def __init__(self,customer_name,customer_surname,customer_id):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.customer_id = customer_id

    def get_cust_info(self):
        self.customer_name=input("Enter your name? ")
        self.customer_surname=input("Enter your surname? ")
        self.customer_id=int(input("Enter your customer ID? "))

    def __str__(self):
        print (f"Name             : {self.customer_name}\
                  \nSurname          : {self.customer_surname}\
                        \nCustomer ID      : {self.customer_id}")
        

customer1=Customer(0,0,0)
customer1.get_cust_info()

item1=Items(0,0,0,0,0)
item1.shopping_cart()

customer1.__str__()
item1.__str__()
