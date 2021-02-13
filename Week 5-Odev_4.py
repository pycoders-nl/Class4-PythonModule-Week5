class Items:
    total_p = 0

    def __init__(self, cust_id=None, item_name=None, price=0, qty=0, total_price=0):
        self.cust_id = cust_id
        self.item_name = item_name
        self.price = price
        self.qty = qty
        self.total_price = total_price
        self.basket = []

    def calculate_discount(self):

        if Items.total_p >= 4000:
            return int(Items.total_p * 0.25)

        if Items.total_p >= 2000:
            return int(Items.total_p * 0.15)

        if Items.total_p < 2000:
            return int(Items.total_p * 0.10)

    def shopping_cart(self):
        print("%" * 22, "YOUR SHOPPING CARD", "%" * 23)

        while True:
            self.item_name = input("Enter a product name: ")
            try:
                self.qty = int(input("Enter quantity: "))
                self.price = int(input("Enter Price: "))
                self.basket.append([self.item_name, self.qty, self.price])
                print("Product added to basket..")
            except:
                print("Enter a integer please..")
            q = input("Do you want to continue shopping? (Y/N)").upper()
            self.total_price = self.price * self.qty
            Items.total_p += self.total_price

            if q == "Y":
                continue
            else:
                n = self.basket
                for i in n:
                    print("\nPRODUCT                           QUANTITY             PRICE"
                          "\n{}                           x   {}                   {} $"
                          "\n------------------------------------------------------------------"
                          .format(i[0], i[1], i[2]))
                self.calculate_discount()
                self.__str__()
                break

    def get_total_amount(self):
        price_tobe_paid = Items.total_p - Items.calculate_discount(self)
        return price_tobe_paid

    def __str__(self):
        print("Your Shopping List :{} "
              "\nSUB TOTAL        :{} $ "
              "\nDISCOUNT         :{} $ "
              "\n=================================================================="
              "\n                                               TOTAL = {} $ "
              .format(self.basket, Items.total_p, Items.calculate_discount(self),
                      Items.get_total_amount(self)))


class Customer:
    customers = []

    def __init__(self, customer_id=None, name=None, last_name=None):
        self.customer_id = customer_id
        self.name = name
        self.last_name = last_name
        self.get_cust_info()

    def get_cust_info(self):
        self.customer_id = input("Enter customer_id:")
        self.name = input("Enter first name:").upper()
        self.last_name = input("Enter last_name:").upper()
        self.customers.append([self.customer_id, self.name, self.last_name])


    def __str__(self):
        for i in Customer.customers:
            print("\nCustomer ID :{} "
                  "\nName        :{} "
                  "\nLast Name   :{}".format(i[0], i[1], i[2]))


c1 = Customer()
print("Customers List: ", Customer.customers)
print()
Customer.__str__(c1)

it1 = Items()
it1.shopping_cart()