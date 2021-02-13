class Product:
    def __init__(self, product_id, product_name, product_purchase_price, product_sale_price):
        self.product_id = str(product_id)
        self.product_name = str(product_name)
        self.product_purchase_price = float(product_purchase_price)
        self.product_sale_price = float(product_sale_price)

    def set_remarks(self):
        self.price_margin = self.product_sale_price - self.product_purchase_price
        if self.price_margin < 0:
            print('Your Loss.....={}'.format(self.price_margin))

        elif self.price_margin > 0:
            print('Your profit.....={}'.format(self.price_margin))
        elif self.price_margin == 0:
            print('Your p.....={}'.format(self.price_margin))


    def set_details(self):
        self.product_id = str(input("Enter product id: "))
        self.product_name = str(input("Enter product name: "))
        self.product_purchase_price = float(input("Enter product purchase price: "))
        self.product_sale_price = float(input("Enter product sale price: "))
        self.product_margin = self.set_remarks()

    def get_details(self):

        all_result = """
Product id: {}
Product name: {}
Product purchase price: {}
Product sale price: {}
Product margin: {}
    """.format(self.product_id, self.product_name, self.product_purchase_price, self.product_sale_price,
               self.product_margin)
        return all_result


p = Product(111, "x", 10, 12)
p.set_details()
p.set_remarks()
print(p.get_details())