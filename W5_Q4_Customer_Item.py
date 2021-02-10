# Class Items :
#
# Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()
#
# calculate_discount():
#
#     total_price = price * qty
#     discount —> 25% if total_price >= 4000
#     discount —> 15% if total_price >= 2000
#     discount —> 10% if total_price < 2000
#     price_tobe_paid = total_price – discount
#
# shopping_cart():
#
#     Let user add items in the shopping basket. Be creative with the items, set their prices as well.
#
# __str__():
#   Print items added and total price nicely.


class Items:
    def __init__(self, cust_id=0 , price=0, total_price=0, qty=0,discount=0,items=0 ):
        self.cust_id= cust_id
        self.total_price = total_price
        self.price = price
        self.items = items
        self.qty = qty
        self.discount = discount

    def __str__(self):
        self.shopping_cart_list = []
        print("  Product Summary  ".center(100, "-"))
        return (f"\nProduct Name: {self.items} \nProduct Price: {self.price}\nProduct Amount: {self.qty}"
                f"\nTotal Discount: {self.discount}\nTotal Payment after discount: {self.price_tobe_paid}")

    def calculate_discount(self):
        self.total_price = self.price * self.qty
        if self.total_price < 2000:
            self.discount = self.total_price * 0.1

        if self.total_price <= 4000:
            self.discount = self.total_price * 0.15

        if self.total_price > 4000:
            self.discount = self.total_price * 0.25

    def shopping_cart(self,x):
        self.items = input("Product to add shopping Basket: ")
        self.price = int(input("Enter the price of Product: "))
        self.qty = int(input("How many do you want to buy? "))
        self.calculate_discount()
        self.get_total_amount()

    def get_total_amount(self):
        self.price_tobe_paid = self.total_price - self.discount
        return self.price_tobe_paid

class Customer:

    def __init__(self, name, surname, age, phone, cust_id, qty):
        self.name = name
        self.qty = qty
        self.surname = surname
        self.age = age
        self.phone = phone
        self.cust_id = cust_id

    def get_cust_info(self):
        self.name = input("Enter your name: ")
        self.surname = input("Enter your surname: ")
        self.age = int(input("Enter your age: "))
        self.phone = input("Enter your phone number: ")

    def __str__(self):
        print("  Customer Summary  ".center(100, "-"))
        return(f"\nCustomer Name: {self.name} \nCustomer Surname: {self.surname}\n"
              f"Customer Age: {self.age} \nCustomer Phone: {self.phone}")

customer1 = Customer(0,"",0 ,0 ,0 ,0)
customer1.get_cust_info()

product1 = Items()
product1.shopping_cart(customer1.cust_id)

print(customer1)
print(product1)
