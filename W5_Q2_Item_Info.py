# Define a class named ItemInfo with the following description:
#
# item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock),
# discount(Discount percentage on the item), net_price(Price after discount)
#
# Methods :
#
#     A member method calculate_discount() to calculate discount as per the following rules:
#     If qty <= 10 —> discount is 0
#     If qty (11 to 20 inclusive) —> discount is 15
#     If qty >= 20 —> discount is 20
#     A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
#     A function called buy() to allow user to enter values for item_code, item, price, qty.
#     Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
#     A function show_all() or similar name to allow user to view the content of all the data members.

class ItemInfo:

    def __init__(self, item_code=0,  price=0, qty=0, net_price=0, discount=0):
        self.item_code = item_code
        self.price = price
        self.qty = qty
        self.net_price = net_price
        self.discount = discount

    def Buy(self):
        self.item_code = input("Urun Kodunu Giriniz: ")
        self.item = input("Urun Adini Giriniz: ")
        self.price = int(input("Urun Fiyatini Giriniz: "))
        self.qty = int(input("Urun Miktarini Giriniz: "))
        self.discount = self.CalculateDiscount()
        self.net_price = self.qty * (self.price - (self.price * self.discount / 100))

    def CalculateDiscount(self):
        if self.qty <= 10:
            self.discount = 0
        elif self.qty <=20:
            self.discount = 15
        else:
            self.discount = 20
        return self.discount

    def ShowData(self,x):
        print("  Siparis Ozeti  ".center(100,"-"))
        print(f"\nUrun Kodu: {item1.item_code} \nUrun Adi:{item1.item}\nUrun Fiyati: {item1.price} "
              f"\nUrun Miktari: {item1.qty} \nIndirimden Onceki Fiyat: {item1.qty*item1.price}"
              f"\nIndirimli Fiyat: {item1.net_price}")

item1 = ItemInfo()

(item1.ShowData(item1.Buy()))

