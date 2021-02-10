from tabulate import tabulate


class ItemInfo:
    def __init__(self):
        self.item_code = 0
        self.item = None
        self.price = None
        self.qty = None
        self.net_price = None
        self.discount = None

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif self.qty <= 20:
            self.discount = 15
        else:
            self.discount = 20

    def buy(self):
        self.item_code = input("enter the item code: ")
        self.item = input("enter the item name: ")
        self.price = float(input("enter the item price: "))
        self.qty = int(input("enter the quantity of stock: "))
        self.calculate_discount()
        self.net_price = self.price-((self.price*self.discount)/100)

    def show_all(self):
        print(tabulate([[self.item, self.item_code, self.qty, self.price, self.net_price]], headers=[
              "Item Name", "Item Code", "Quantity of Stock", "Item Price", "Item Net Price"]))


item = ItemInfo()
item.buy()
item.show_all()
