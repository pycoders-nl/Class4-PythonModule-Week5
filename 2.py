class ItemInfo:
    def __init__(self):
        self.item_code = 0
        self.item = ''
        self.price = None
        self.qty = None
        self.discount = None
        self.net_price = None
        
        self.buy()
        self.calculate_discount()
        self.show_all()

    def buy(self):
        self.item_code = int(input("Item kodu girin: "))
        self.item = input("Item name giriniz : ")
        self.price = float(input("Itemlerin herbirinin fiyatini giirniz: "))
        self.qty = int(input(f"Kac adet {self.item} satin alicaksiniz: "))

        
    def calculate_discount(self):
        if self.qty >= 20:
            self.discount = 0.2
            self.net_price = self.price * self.qty * 0.8
        elif self.qty >= 11:
            self.discount = 0.15
            self.net_price = self.price * self.qty * 0.85
        else :
            self.discount = 0
            self.net_price = self.price * self.qty


    def show_all(self):
        print(f"""
    Item Code: {self.item_code}
    Item Name: {self.item}
    Price: {self.price}
    QTY: {self.qty}
    Discount: ${self.net_price*self.discount}
    Total: ${self.net_price}
        """)

s = ItemInfo()