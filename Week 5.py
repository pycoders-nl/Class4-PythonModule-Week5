#!/usr/bin/env python
# coding: utf-8

# # Question 1

# # Create the class Society with following information:
# 
# society_name, house_no, no_of_members, flat, income
# 
# Methods :
# 
# An __init__ method to assign initial values of society_name, flat, house_no, no_of_members, income
# input_data() To read information from members
# allocate_flat() To allocate flat according to income using the below table.
# show_data() to display the details of the entire class.
# image
# 
# [image.png](attachment:image.png)

# In[ ]:


# Solution 1

class Society:
    def __init__(self, name,house_no, no_of_members, income):
        self.name = name
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.income = int(income)
    
    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = "A type"
        elif self.income >= 20000:
            self.flat = "B type"
        elif self.income >= 15000:
            self.flat = "C type"
        else:
            self.flat = "D type"
        return self.flat
            
    def input_data(self):
        self.name = input("Please enter the name of the society: ")
        self.house_no = input("Please enter the amount of the houses: ")
        self.no_of_members = input("Please enter the amount of the members: ")
        self.income = int(input("Please enter the income: "))
        
    def see(self):
        print("The {} society has {} houses and {} members. ".format(self.name,self.house_no,self.no_of_members) )
        print("In addition, the average income of the society is {} and the suitable flat type is {}.".format(self.income, self.flat))
        

society1 = Society(0,0,0,1)
society1.input_data()
society1.allocate_flat()
society1.see()


# 
# # Question 2:

# Define a class named ItemInfo with the following description:
# 
# item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item), net_price(Price after discount)
# 
# Methods :
# 
# A member method calculate_discount() to calculate discount as per the following rules:
# If qty <= 10 —> discount is 0
# If qty (11 to 20 inclusive) —> discount is 15
# If qty >= 20 —> discount is 20
# A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
# A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
# A function show_all() or similar name to allow user to view the content of all the data members.

# In[ ]:


# Solution 2

class ItemInfo:
    
    def __init__(self,item_code, item, price, qty):
        self.item_code = item_code
        self.item = item
        self.price = int(price)
        self.qty = int(qty)
        
    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
            
        elif self.qty <= 20:
            self.discount = 15
            
        else:
            self.discount = 20
            
        return self.discount
    
    def calculate_net_price(self):
        self.costs = (self.price * self.qty * (100-self.discount))/100
        return self.costs
    
    def buy(self):
        self.item_code = input("Please enter the item code: ")
        self.item = input("Please enter the name of the item: ")
        self.price = int(input("Please enter the price: "))
        self.qty = int(input("Please enter the quantity: "))
        
    def see(self):
        print("The item_code: {} ".format(self.item_code))
        print("The item: {} ".format(self.item))
        print("The price: {}".format(self.price))
        print("The quantity: {}".format(self.qty))
        print("The discount is {} %.".format(self.discount))
        print("The net costs: {}".format(self.costs))
        
it1=ItemInfo(0,1,1,1)
it1.buy()
it1.calculate_discount()
it1.calculate_net_price()
it1.see()
        


# # Question 3:

# Define a class named Product with the following specifications:
# 
# Data members:
# product_id – A string to store product.
# product_name - A string to store the name of the product.
# product_purchase_price – A decimal to store the cost price of the product.
# product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
# Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
# 
# Methods :
# 
# A constructor to intialize all the data members with valid default values.
# A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
# image
# 
# A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
# A method get_details() that displays all the data members.

# In[ ]:


#Solution 3

class Product:
    def __init__(self, product_id, product_name, purchase_price, sale_price):
        self.product_id = product_id
        self.product_name = product_name
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        
    def set_details(self):
        self.product_id = input("Please enter the product ID: ")
        self.product_name = input("Please enter the name of the product: ")
        self.purchase_price = int(input("Please enter the purchase price: "))
        self.sale_price = int(input("Please enter the sale price: "))
        self.margin = self.sale_price - self.purchase_price
        
    def set_remarks(self):
        if self.margin == 0:
            pass
        elif self.margin < 0:
            self.remark = "Loss"
        else:
            self.remark = "Profit"
        
        return self.remark
    
    def get_details(self):
        print("The product ID: {} ".format(self.product_id))
        print("The name of the product: {} ".format(self.product_name))
        print("The purchase price: {}".format(self.purchase_price))
        print("The sale price: {}".format(self.sale_price))
        print("The margin: {}".format(self.margin))
        print("The remark: {}".format(self.remark))

product1= Product(0,1,1,1)        
product1.set_details()
product1.set_remarks()
product1.get_details()        


# # Question 4:

# Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
# 
# Class Items :
# Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()
# 
# calculate_discount():
# 
# total_price = price * qty
# discount —> 25% if total_price >= 4000
# discount —> 15% if total_price >= 2000
# discount —> 10% if total_price < 2000
# price_tobe_paid = total_price – discount
# shopping_cart():
# 
# Let user add items in the shopping basket. Be creative with the items, set their prices as well.
# __str__():
# 
# Print items added and total price nicely.
# Class Customer :
# Methods: __init__(), get_cust_info() this is optional, __str__()
# 
# Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in __init__() and pass customer information as arguments while creating a customer object.
# 
# __str__():
# 
# Print customer information and price nicely.
# Find a way to link two classes. For example, instances of both classes may have a customer number. With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number such as price, quantity or so.
# 
# In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.
# 
# Simple example:
# 
# Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
# 
# shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]
# 
# Crate a few customers and print their information (Personal and shopping info).

# In[12]:


#Solution 4:

class Items:
    def __init__(self, customer_id=0 , price=0, total_price=0, qty=0,discount=0,product=0 ):
        self.customer_id= customer_id
        self.total_price = total_price
        self.price = price
        self.product = product
        self.qty = qty
        self.discount = discount

    def __str__(self):
        self.shopping_cart_list = []
        print("  Product Information  ".center(70, "-"))
        return (f"\nProduct Name: {self.product} \nProduct Price: {self.price}\nProduct Amount: {self.qty}"
                f"\nTotal Discount: {self.discount}\nTotal Payment after discount: {self.payment}")

    def calculate_discount(self):
        self.total_price = self.price * self.qty
        if self.total_price < 2000:
            self.discount = self.total_price * 0.1

        if self.total_price <= 4000:
            self.discount = self.total_price * 0.15

        if self.total_price > 4000:
            self.discount = self.total_price * 0.25

    def shopping_cart(self,x):
        self.product = input("Please enter a product name: ")
        self.price = int(input("Please enter the price of the product: "))
        self.qty = int(input("Please enter the quantity of the product: "))
        self.calculate_discount()
        self.get_total_amount()

    def get_total_amount(self):
        self.payment = self.total_price - self.discount
        return self.payment

class Customer:

    def __init__(self, name, surname, customer_id, qty):
        self.name = name
        self.qty = qty
        self.surname = surname
        self.customer_id = customer_id

    def get_cust_info(self):
        self.name = input("Enter your name: ")
        self.surname = input("Enter your surname: ")

    def __str__(self):
        print("  Customer Information  ".center(70, "-"))
        return(f"\nName: {self.name} \nSurname: {self.surname}\n")


customer1 = Customer("","",1,0)
customer1.get_cust_info()

product1 = Items()
product1.shopping_cart(customer1.customer_id)

print(customer1)
print(product1)
        


# In[ ]:




