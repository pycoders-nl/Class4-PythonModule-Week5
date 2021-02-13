class ItemInfo:
    def __init__(self, item_code=0, item=0, price=0, qty=0, discount=0, net_price=0):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price

    def calculate_discount(self):
        if int(self.qty) <= 10:
            self.discount = 0
        elif 11 <= int(self.qty) <= 20:
            self.discount = 15
        elif int(self.qty) >= 20:
            self.discount = 20
        net_price = int(self.price) * int(self.qty) - int(self.discount)
        return net_price

    def buy(self):
        self.item_code = input("Enter a Item Code:")
        self.item = input("Enter a item name:")
        self.price = input("Enter a price:")
        self.qty = input("Enter a quantity of stock:")
        ItemInfo.calculate_discount(self)

    def show_all(self):
        print("%%%%%%% All The Data Members %%%%%%%")
        print("Item Code        : {} "
              "\nitem name        : {} "
              "\nprice            : {} "
              "\nquantity in stock: {} "
              "\ndiscount         : {} "
              "\nnet_price        : {} "
              .format(self.item_code, self.item, self.price, self.qty, self.discount, ItemInfo.calculate_discount(self)))

x = ItemInfo()
x.buy()
x.calculate_discount()
x.show_all()