class Item_Info:
    def __init__(self, item_code = 0, price = None, qty = None, net_price = None, discount = None):
        self.item_code = item_code
        self.price = price
        self.qty = qty
        self.net_price = net_price
        self.discount = discount
    
    def calculate_discount(self) :
        if(self.qty <= 10):
            self.discount = 0
        elif 11 <= self.qty < 20:
            self.discount = 15
        else:
            self.discount = 20
        
        self.net_price = self.price * self.qty - self.discount
    
    def buy(self):
        while True :
            try :
                self.item_code = int(input('Enter the Items Code in Nummbers : '))
                self.item = input('Enter the Name of the Item : ')
                self.price = int(input('Enter the Price of the Item in Nummbers : '))
                self.qty =int(input('Enter how Items you want to buy in Nummbers (Quantity) : '))
            except ValueError:
                print('Please Enter number where it requires it')
            except :
                print('There was an Error. Please!! Try Again') 

        self.calculate_discount()
    
    def show_all(self):
        s = ''
        s += '\nCode of the Item is ' + str(self.item_code)
        s += '\nName of the Item is ' + self.item
        s += '\nPrice of the Item is' + str(self.price)
        s += '\nQuantity of the Item is' + str(self.qty)
        s += '\nThe discount you got is' + str(self.discount)
        s += "\nThe Net price you're going to pay is " + str(self.discount)

        print(s)