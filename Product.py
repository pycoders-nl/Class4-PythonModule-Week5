'''
Define a class named Product with the following specifications:
Data members:
product_id – A string to store product.
product_name - A string to store the name of the product.
product_purchase_price – A decimal to store the cost price of the product.
product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as
(product_sale_price - product_purchase_price)
Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods :
A constructor to intialize all the data members with valid default values.
A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and
 sets Remarks as mentioned below :
Margin            Remarks
<0 negative        Loss
>0 positive        Profit
A method set_details() to accept values for product_id. product_name, product_purchase_price,
product_sale_price and invokes SetRemarks() method.
A method get_details() that displays all the data members.
Author= Bulent Caliskan  date= 08/02/2021
'''


class Product:
    def __init__(self, product_id, product_name, product_purchase_price, product_sale_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price

    def set_remarks(self):
        if (self.product_sale_price - self.product_purchase_price) < 0: return "Loss"
        else: return "Profit"

    def set_details(self):
        try:
            self.product_id = input("Enter id of product ? ")
            self.product_name = input("Enter name of product ? ")
            self.product_purchase_price = int(input("Enter product purchase price ? "))
            self.product_sale_price = int(input("Enter product sale price ? "))

        except:
            print("Please enter the value you entered correctly. ")

    def get_details(self):
        print (f"Product ID             : {self.product_id}\
                   \nProduct name           : {self.product_name}\
                       \nProduct purchase price : {self.product_purchase_price}\
                          \nProduct sale price     : {self.product_sale_price}\
                             \nSale price margin      : {Product.set_remarks(self)} ")


product1 = Product(0, 0, 0, 0)
product2 = Product(0, 0, 0, 0)

product1.set_details()
product1.get_details()

product2.set_details()
product2.get_details()