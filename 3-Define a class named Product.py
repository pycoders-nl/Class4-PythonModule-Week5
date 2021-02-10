class Product:
    product_id = 0
    product_name = "None"
    product_purchase_price = 0
    product_sale_price = 0
    remarks = "None"

    def __int__(self):
        self.product_id = 0
        self.product_name = "None"
        self.product_purchase_price = 0
        self.product_sale_price = 0
        self.remarks = "None"

    def set_remarks(self):
        if self.product_sale_price - self.product_purchase_price > 0:
            self.remarks = "Profit"
        elif self.product_sale_price - self.product_purchase_price < 0:
            self.remarks = "Loss"

    def set_details(self, product_id, product_name, product_purchase_price, product_sale_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price
        self.set_remarks()

    def get_details(self):
        print("\n Product id: " + str(self.product_id) + "\n Product name: " + self.product_name + "\n Product Purchase Price: " +
              str(self.product_purchase_price) + "\n Product Sale Price " + str(
            self.product_sale_price) + "\n Remarks: " + self.remarks)


Example_class = Product()
Example_class.set_details(1, "pen", 10, 12)
Example_class.get_details()
Example_class.set_details(2, "notebook", 10, 8)
Example_class.get_details()
