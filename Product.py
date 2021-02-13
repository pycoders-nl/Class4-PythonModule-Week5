

class Product:

    def __init__(self):
        self.Pid = ""
        self.Pname = ""
        self.Pcostprice = 0.0
        self.Psellprice = 0.0
        self.Margin = 0.0
        self.Remarks = ""

    def GetDetails(self):

        self.Pid = input("Enter Product ID:")
        self.Pname = input("Enter Product Name :")
        self.Pcostprice = input("Enter Cost Price")
        self.Psellprice = input("Enter Selling Price")
        self.SetRemarks()


    def SetRemarks(self):
        self.Margin = int(self.Psellprice) - int(self.Pcostprice)
        if self.Margin < 0:
            self.SetRemarks = "Loss "
        else:
            self.SetRemarks = "Profit"

    def SetDetails(self):

        print ("Product ID:", self.Pid)
        print ("Product Name:", self.Pname)
        print("Cost Price:", self.Pcostprice)
        print("Selling Price:", self.Psellprice)
        print("Margin:", self.Margin)
        print("Incurred:",  self.SetRemarks)

    def showAll(self):
        return  """ Product ID: {} Product Name: {} 
        Cost Price: {} 
        Selling Price: {} 
        Margin: {} 
        Incurred: {}
         """.format(self.Pid,self.Pname,self.Pcostprice,self.Psellprice, self.Margin, self.SetRemarks)

new_product=Product()
new_product.GetDetails()
print(new_product.showAll())

