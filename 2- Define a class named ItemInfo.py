"""
Define a class named ItemInfo with the following description:

item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock),
discount(Discount percentage on the item), net_price(Price after discount)

Methods :

* A member method calculate_discount() to calculate discount as per the following rules:
* If qty <= 10 —> discount is 0
* If qty (11 to 20 inclusive) —> discount is 15
* If qty >= 20 —> discount is 20
* A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
* A function called buy() to allow user to enter values for item_code, item, price, qty.
  Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
* A function show_all() or similar name to allow user to view the content of all the data members.
"""


class ItemInfo:
    """A constructor init method to assign the initial values"""
    def __init__(self, item_code=0, item='null', price=0, qty=0, discount=0, net_price=0):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price

    def buy(self, ):
        """allow user to enter values"""
        self.item_code = input("enter item_code: ")
        self.item = input("enter item: ")
        self.price = int(input("enter price: "))
        self.qty = int(input("enter qty: "))

    def calculate_discount(self,):
        """allocate flat according to income"""
        if self.qty <= 10: self.discount = 0
        elif 11 < self.qty <= 20: self.discount = 15
        elif self.qty > 20: self.discount = 20
        self.net_price = self.price * self.qty - self.discount

    def show_all(self, ):
        """display the details of the entire class"""
        return print('item_code : {}\n'
                     'item      : {}\n'
                     'price     : {}\n'
                     'qty       : {}\n'
                     'discount  : {}\n'
                     'net_price : {}\n'
                     .format(self.item_code, self.item, self.price, self.qty, self.discount, self.net_price))


"""Test"""

item = ItemInfo(1)
item.buy()
item.show_all()
item.calculate_discount()
item.show_all()
