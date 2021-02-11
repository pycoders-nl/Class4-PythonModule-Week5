class ItemInfo():
    def __init__(self, price = 0, qty = 0, net_price = 0, discount = 0, item_code = 0):
        self.item_code = item_code
        self.price = price
        self.qty = qty
        self.net_price = net_price
        self.discount = discount

    def calculate_discount(self):
        if self.qty > 20:
            self.discount = 20
        if 11 <= self.qty <= 20:
            self.discount = 15
        if self.qty <= 10:
            self.discount = 0

        return
    
    def buy(self):
        self.item_code = input('Enter item code: ')
        self.item = input('Enter the item: ')
        self.price = float(input('Enter the price of the {}: '.format(self.item)))
        self.qty = int(input('Enter the quantity of the {}: '.format(self.item)))
        self.discount = self.calculate_discount()
        # self.net_price = (self.qty * (self.price - (self.price * (self.discount/100))))
        self.net_price = float((self.qty * ((100-self.discount)*self.price))  # Diger islem yolu
    
    def show_all(self):
        all_results = ("item code: ",self.item_code,'item name: ',self.item, 'item price: ',self.price, 'item quantity: ',self.qty, 'item discount: ',self.discount,'Net price: ',self.net_price)
        return all_results
    
my_item1 = ItemInfo()
my_item1.buy()
print(my_item1.show_all())