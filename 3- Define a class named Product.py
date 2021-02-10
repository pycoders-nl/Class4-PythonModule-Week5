"""
Define a class named Product with the following specifications:

Data members:
* product_id – A string to store product.
* product_name - A string to store the name of the product.
* product_purchase_price – A decimal to store the cost price of the product.
* product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)

Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.

Methods :

A constructor to intialize all the data members with valid default values.
A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
image

A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
A method get_details() that displays all the data members.
"""


class Product:
    """"""
    def __init__(self, product_id='', product_name='', product_purchase_price=0, product_sale_price=0):
        self.product_id = str(product_id)
        self.product_name = str(product_name)
        self.product_purchase_price = float(product_purchase_price)
        self.product_sale_price = float(product_sale_price)

    def set_remarks(self):
        """"""
        self.margin = (self.product_sale_price - self.product_purchase_price)
        if self.margin < 0:
            self.remarks = 'Loss'
        elif self.margin > 0:
            self.remarks = 'Profit'

    def set_details(self):
        """"""
        self.product_id = str(input("Enter product_id: "))
        self.product_name = str(input("Enter product_name: "))
        self.product_purchase_price = float(input("Enter product_purchase_price: "))
        self.product_sale_price = float(input("Enter product_sale_price: "))
        self.set_remarks()

    def get_details(self, ):
        """"""
        return print('product_id                : {}\n'
                     'product_name              : {}\n'
                     'product_purchase_price    : {}\n'
                     'product_sale_price        : {}\n'
                     'remarks                   : {}\n'
                     .format(self.product_id, self.product_name, self.product_purchase_price, self.product_sale_price, self.remarks))


"""Test"""

Product1 = Product()
Product1.set_details()
Product1.get_details()

