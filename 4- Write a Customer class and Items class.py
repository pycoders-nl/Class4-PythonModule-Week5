class Items:
    item_name = "new"
    item_price = 0

    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def get_price(self):
        return self.item_price


class Customer:
    customer_id = 0
    name = "name"
    lastname = "lastname"

    def __init__(self, customer_id, name, lastname):
        self.customer_id = customer_id
        self.name = name
        self.lastname = lastname


class Shopping_Card:
    one_customer = None
    line_item_list = []

    def __init__(self, customer):
        assert isinstance(customer, Customer)
        self.one_customer = customer
        self.line_item_list = []

    def __str__(self):
        text = self.one_customer.name + " " + self.one_customer.lastname + " " + \
               str(self.one_customer.customer_id) + "\n" + \
               "YOUR SHOPPING CARD" + "\n_______________________________\n\n"


        for line_item in self.line_item_list:
            item = line_item["product"]
            assert isinstance(item, Items)
            text = text + item.item_name + "   x   " + str(line_item["count"]) + "      " + str(line_item["count"] * item.item_price) + "\n"

        text = text + "\nSUB TOTAL             " + str(self.total_price())
        text = text + "\nDISCOUNT              " + str(self.total_price()*self.calculate_discount()/100) + "    %" + str(self.calculate_discount())
        text = text + "\n_______________________________"
        text = text + "\nTOTAL                 " + str(self.price_to_be_paid())
        return text

    def create_line_item(self, item, count):
        assert isinstance(item, Items)
        line_item_dict = dict()
        line_item_dict["product"] = item
        line_item_dict["count"] = count
        self.line_item_list.append(line_item_dict)

    def total_price(self):
        total_price = 0
        for line_item_dict in self.line_item_list:
            item = line_item_dict["product"]
            # assert isinstance(item, Items)
            total_price = total_price + line_item_dict["count"] * item.get_price()
        return total_price

    def calculate_discount(self):
        total_price = self.total_price()
        if total_price >= 4000:
            return 25
        elif total_price >= 2000:
            return 15
        elif total_price < 2000:
            return 10

    def price_to_be_paid(self):
        discount = self.calculate_discount()
        total_price = self.total_price()
        return (total_price*(100-discount))/100


class Shop:
    items_list = []
    customer_list = []
    shopping_card_list = []


shop = Shop

t_shirt = Items("t-shirt ", 100)
shirt = Items("shirt   ", 300)
shoes = Items("shoes   ", 500)
pant = Items("pant    ", 400)

customer_1 = Customer(1001, "John", "Traolta")
shop.customer_list.append(customer_1)
customer_2 = Customer(1002, "Coby", "Brien")
shop.customer_list.append(customer_2)
customer_3 = Customer(1003, "Micheal", "Dan")
shop.customer_list.append(customer_3)
customer_4 = Customer(1004, "Susan", "Farrel")
shop.customer_list.append(customer_4)

new_shop_card = Shopping_Card(customer_1)
shop.shopping_card_list.append(new_shop_card)
new_shop_card.create_line_item(t_shirt, 2)
new_shop_card.create_line_item(shirt, 3)
new_shop_card.create_line_item(shoes, 2)
new_shop_card.create_line_item(pant, 5)

new_shop_card2 = Shopping_Card(customer_2)
new_shop_card2.create_line_item(t_shirt, 3)
new_shop_card2.create_line_item(shirt, 1)
new_shop_card2.create_line_item(shoes, 1)
new_shop_card2.create_line_item(pant, 2)


print(new_shop_card)

print(new_shop_card2)
