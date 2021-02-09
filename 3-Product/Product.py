class Product:
    def __init__(self, product_id = None, product_name= None, product_purchase_price = None, product_sale_price = None, sale_price_margin = None ):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price
        self.sale_price_margin = sale_price_margin
    
    def set_remarks(self):
        if self.product_sale_price - self.product_purchase_price < 0:
            self.sale_price_margin = 'Loss'
        else:
            self.sale_price_margin = 'Profit'
        
    def set_details(self):
        while True:
            try:
                self.product_id = int(input('Enter the Product ID (Number):'))
                self.product_name = input('Enter the Product name:')
                self.product_purchase_price = int(input('Enter the Product Purchase Price (Number):'))
                self.product_sale_price = int(input('Enter the Product Sale Price (Number):'))
                break
            except ValueError:
                print("Please enter numbers in the right place.")
            except :
                print('There was an error. Please, truy again!!')
    
    def get_details(self):
        s = ''
        s += 'Product ID: '+ str(self.product_id) 
        s += '\nProduct Name: '+ self.product_name 
        s += '\nProduct Purchase Price: '+ str(self.product_purchase_price) 
        s += '\nProduct Sale Price: '+ str(self.product_sale_price) 
        s += '\nProduct Margin: '+ self.sale_price_margin 
        return s

