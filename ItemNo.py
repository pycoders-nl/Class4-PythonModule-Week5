
class ItemInfo:
    def __init__(self, ItCode=0, Item=0, Price=0, Qty=0, Discount=0, Netprice=0):
        self.ItCode=ItCode
        self.Item=Item
        self.Price=Price
        self.Qty=Qty
        self.Discount=Discount
        self.Netprice=Netprice
    def Buy(self):
        self.ItCode= input("Enter Item Code")
        self. Item= input("Enter Item Name")
        self.Price= int(input("Enter Price"))
        self.Qty= int(input("Enter Quantity"))
        self.Discount = self.FindDisc()
        self.Netprice = int(self.Price*(100-self.Discount)/100)
    def FindDisc(self):
        if self.Qty <= 10:
            self.Discount = 0
        elif  11 <=  self.Qty < 20:
            self.Discount = 15
        else:
            self.Discount = 20

        return self.Discount

    def ShowAll(self):
        print ("Item Code",self.ItCode)
        print ("tem Name",self.Item)
        print ("Price",self.Price)
        print ("Discount",self.Discount)
        print ("NetPrice",self.Netprice)

    def show_All(self):
        return  """ Item code: {} Item name: {} Item price: {} Item quantity: {} 
Item Discount: {} percent Discounted item price: {}
         """.format(self.ItCode,self.Item,self.Price,self.Qty, self.Discount, self.Netprice)


new_item = ItemInfo()
new_item.Buy()
print(new_item.show_All())

