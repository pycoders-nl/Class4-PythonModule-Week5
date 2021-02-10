class product:
    def __init__(self,product_id,product_name,product_purchase_price,product_sale_price,):
        self.product_id=product_id
        self.product_name=product_name
        self.product_purchase_price=product_purchase_price
        self.product_sale_price=product_sale_price

    def set_remarks(self):
        self.end_price=self.product_sale_price - self.product_purchase_price
        if self.end_price<0:
            return "Loss"
        elif self.end_price>0:
            return "Profit"

    def set_details(self):
        self.product_id=2546
        self.product_name="Phone"
        self.product_purchase_price=420
        self.product_sale_price=500
        self.pr=self.set_remarks()

        
    def get_details(self):
        print("product_id:", self.product_id, ",product_name:", self.product_name, ",product_purchase_price:", self.product_purchase_price, ",product_sale_price:", self.product_sale_price,)


x=product(2546,"phone",420,500)
print(x.set_remarks())
print(x.set_details())
print(x.get_details())