# Question 4:
# Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.

# Class Items :
# Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()

# calculate_discount():

# total_price = price * qty
# discount —> 25% if total_price >= 4000
# discount —> 15% if total_price >= 2000
# discount —> 10% if total_price < 2000
# price_tobe_paid = total_price – discount
# shopping_cart():

# Let user add items in the shopping basket. Be creative with the items, set their prices as well.
# __str__():

# Print items added and total price nicely.
# Class Customer :
# Methods: __init__(), get_cust_info() this is optional, __str__()

# Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in __init__() and pass customer information as arguments while creating a customer object.

# __str__():

# Print customer information and price nicely.
# Find a way to link two classes. For example, instances of both classes may have a customer number. With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number such as price, quantity or so.

# In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.

# Simple example:

# Customer1 = [name : Jack, last_name : Russel, customer_id : 123]

# shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]

# Crate a few customers and print their information (Personal and shopping info).

class Items:
    def __init__(self,price=0,qty=0):
        self.price = price
        self.qty = qty

    def __str__(self):
        all_result = """
Customer id: {}, Item name: {}, Item price: {}, Item quantity: {}, Total price: {}, Total discount {} procent, To be paid after discount: {}
    """.format(self.customer_id,self.item_name, self.price, self.qty, self.total_price,self.discount, self.price_to_be_paid)
        return all_result

    def calculate_discount(self):
        self.total_price = self.price * self.qty
        if self.total_price >= 4000:
            self.discount = 25
        elif 2000 <= self.total_price < 4000:
            self.discount = 15
        elif self.total_price < 2000:
            self.discount = 10

    def shopping_cart(self):
        """ Users can add new items here """
        self.customer_id = int(input("Enter your customer id: "))
        self.item_name = input("Enter item name: ")
        self.price = int(input(f"Enter price of {self.item_name}: "))
        self.qty = int(input(f"Enter quantity of {self.item_name}: "))
        self.calculate_discount()
        self.get_total_amount()

    def get_total_amount(self):
        self.price_to_be_paid = self.total_price - self.total_price*(self.discount/100)
        return self.price_to_be_paid

class Customer:
    def __init__(self, customer_id, name, surname):
        self.customer_id = customer_id
        self.name = name
        self.surname = surname
        pass

    def __str__(self):
        return f"Customer name: {self.name}, Surname: {self.surname}, Customer id: {self.customer_id}"

    def get_customer_info(self):
        self.name = input("Enter your name: ")
        self.surname = input("Enter your surname: ")
        self.customer_id = int(input("Enter your customer id: "))

def merge(ob1,ob2):
    result = """ 
{}
{}
    """.format(ob1,ob2)
    return result

my_customer1 = Customer(120,"Kerim","Sak")
my_customer1.get_customer_info()

my_item1 = Items()
my_item1.shopping_cart()

my_customer2 = Customer(100,"Ahmet","Uzunoglu")
my_customer2.get_customer_info()

my_item2 = Items()
my_item2.shopping_cart()

inst_1 = merge(my_customer1, my_item1)
print(inst_1)

inst_2 = merge(my_customer2, my_item2)
print(inst_2)
