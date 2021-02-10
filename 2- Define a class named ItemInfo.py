class ItemInfo:
    item_code = 0
    price = None
    qty = None
    Net_price = None
    discount = None

    def __init__(self):
        self.item_code = 0
        self.price = None
        self.qty = None
        self.net_price = None
        self.discount = None

    def buy(self):
        self.item_code = int(input("Please enter an item code: "))
        self.item = input("Please enter an item name: ")
        self.price = int(input("Please enter a price: "))
        self.qty = int(input("Please enter quantity: "))

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        if 11 <= self.qty < 20:
            self.discount = 15
        if self.qty > 20:
            self.discount = 20

    def show_all(self):
        print("item_code: " +
              str(self.item_code) + " price: " +
              str(self.price) + " quantity: " +
              str(self.qty) + " net price: " +
              str(self.net_price) + " discount" +
              str(self.discount)
              )

    def net_price_calculate(self):
        self.net_price = ((self.price * self.qty) * (100 - self.discount)) / 100


S = ItemInfo()
S.buy()
S.calculate_discount()
S.net_price_calculate()
S.show_all()
S.buy()
S.calculate_discount()
S.net_price_calculate()
S.show_all()
S.buy()
S.calculate_discount()
S.net_price_calculate()
S.show_all()
