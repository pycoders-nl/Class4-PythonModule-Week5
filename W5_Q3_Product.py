# Define a class named Product with the following specifications:
# Data members:
#
#     product_id – A string to store product.
#     product_name - A string to store the name of the product.
#     product_purchase_price – A decimal to store the cost price of the product.
#     product_sale_price – A decimal to store Sale Price Margin -
#
#     A decimal to be calculated
# as (product_sale_price - product_purchase_price)
#
# Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.

#
#     A constructor to intialize all the data members with valid default values.
#     A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price)
#     and sets Remarks as mentioned below :


class Product():
    def __init__(self, p_id, p_name, p_purchase_price, p_sale_price ):
        self.p_id = p_id
        self.p_name = p_name
        self.p_purchase_price = p_purchase_price
        self.p_sale_price = p_sale_price

    def set_remarks(self):
        if self.p_sale_price - self.p_purchase_price > 0:
            return "Profit"
        else:
            return "Loss"

    def set_details(self):
        self.p_id = input("Enter Product ID: ")
        self.p_name = input("Enter Product Name: ")
        self.p_purchase_price = int(input("Enter Product Purchase Price: "))
        self.p_sale_price = int(input("Enter Product Sale Price: "))
        self.set_remarks()


    def get_details(self,x):
        print("  Product Summary  ".center(100, "-"))
        print(f"\nProduct ID: {product1.p_id} \nProduct Name:{product1.p_name}\nProduct Purchase Price:"
              f" {product1.p_purchase_price} \nProduct Sale Price: {product1.p_sale_price} \nProduct Remarks:"
              f" {product1.set_remarks() }")

product1 = Product(0,"" ,0 , 0)

product1.get_details(product1.set_details())