# Question 2:
# Define a class named ItemInfo with the following description:

# item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item), net_price(Price after discount)

# Methods :

# A member method calculate_discount() to calculate discount as per the following rules:
# If qty <= 10 —> discount is 0
# If qty (11 to 20 inclusive) —> discount is 15
# If qty >= 20 —> discount is 20
# A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
# A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
# A function show_all() or similar name to allow user to view the content of all the data members.


class ItemInfo:

    def __init__(self, price =0, qty = 0, net_price = 0, discount = 0,  item_code = 0 ):
        self.item_code = item_code
        self.price = price
        self.qty = qty
        self.net_price = net_price
        self.discount = discount 
    
    def calculate_Discount(self):
        """ Calculates discount as per the following rules:
            # If qty <= 10 —> discount is 0
            # If qty (11 to 20 inclusive) —> discount is 15
            # If qty >= 20 —> discount is 20 """

        if self.qty <= 10:
            self.discount = 0
        if 11 <= self.qty <= 20:
            self.discount = 15
        if self.qty > 20:
            self.discount = 20
        return self.discount

    def buy(self):
        """ Allows user to enter values for item_code, item, price, qty"""
        self.item_code = input("Enter item code: ")
        self.item = input("Enter the item: ")
        self.price = float(input(f"Enter the price of the {self.item}: "))
        self.qty = int(input(f"Enter the quantity of the {self.item}: "))
        self.discount = self.calculate_Discount() # Calls function calculate_discount() 
        self.net_price = (self.qty * (self.price - (self.price*(self.discount/100)))) # Calculates Discount with Procent

    def showAll(self):
        """ Allows user to view the content of all the data members. """
        all_result = """ 
Item code: {}
Item name: {}
Item price: {}
Item quantity: {}
Item Discount: {} procent
Item Price after discount: {}
         """.format(self.item_code,self.item,self.price,self.qty, self.discount, self.net_price)
        return all_result

my_item1 = ItemInfo()
my_item1.buy()
print(my_item1.showAll())

my_item2 = ItemInfo()
my_item2.buy()
print(my_item2.showAll())

my_item3 = ItemInfo()
my_item3.buy()
print(my_item3.showAll())