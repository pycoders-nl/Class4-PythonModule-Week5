class Customer:
    def __init__(self, name, last_name, customer_id):
        self.name = name
        self.last_name = last_name
        self.customer_id = customer_id

    def __str__(self):
        print('''
        Customer Name : {} {}
        Customer Id : {}
        '''.format(self.name, self.last_name, self.customer_id))


class Items:
    products = {
        '1. ADATA 16gb Ram': 110,
        '2. Kingston 16gb Ram': 150,
        '3. Corsair 16gb Ram': 130,
        '4. RTX 3090 24GB Graphics Card': 1700,
        '5. RTX 3080 10GB Graphics Card': 1300,
        '6. RTX 2060 Ti 6GB Graphics Card': 450,
        '7. RTX 1650 Super 4GB Graphics Card': 250,
        '8. Intel core i9 10900k': 600,
        '9. Intel core i9 10850k': 440,
        '10. Intel core i7 10900k': 380,
        '11. Intel core i7 10700k': 330,
        '12. Intel core i5 10900k': 280,
        '13. Intel core i5 10800k': 230,
        '14. Kingston nvme 1tb ssd': 110,
        '15. Samsung nvme 1tb ssd': 130,
        '16. Western Digital nvme 1tb ssd': 120,
        '17. Kingston nvme 512gb ssd': 80,
        '18. Samsung nvme 512gb ssd': 95,
        '19. Western Digital nvme 512gb ssd': 85,
        '20. MSI x570 Mother Board': 680,
        '21. MSI z490 Unify': 420,
        '22. MSI z390': 320,
        '23. Rog Strix': 200
    }

    def __init__(self, customer_id=0, items={}, total_price=0, discount=0, price_to_be_paid=0):
        self.customer_id = customer_id
        self.items = items
        self.total_price = total_price
        self.discount = discount
        self.price_to_be_paid = price_to_be_paid

    def calculate_discount(self):
        if self.total_price >= 4000:
            self.discount = 25
        elif 2000 <= self.total_price < 4000:
            self.discount = 15
        elif self.total_price < 2000:
            self.discount = 10
        self.discount_amount = self.total_price * self.discount / 100

    def shopping_cart(self):
        print(self.products)
        items_sold = list(self.products.keys())
        while True:
            while True:
                try:
                    item = int(input(
                        'Please choose an item from the list above (Choose the number in front of the item): '))
                    if 1 <= item <= len(items_sold):
                        break
                    else:
                        print(
                            'Choose an item from the list depending on the number. You cannot choose an item which is not in the list')
                except ValueError:
                    print('Please Enter a Number')
                except:
                    print('Something Went wrong')

            while True:
                try:
                    qty = int(input(
                        'How many of them do you want to buy? (Enter a number): '))
                    break
                except ValueError:
                    print('Please Enter a Number')
                except:
                    print('Something Went wrong')

            chosen_item = items_sold[item - 1]
            print('Chosen item : {} \nPrice of the item : {}'.format(
                chosen_item, self.products[chosen_item]))

            if chosen_item in self.items:
                self.items[chosen_item] += qty
            else:
                self.items[chosen_item] = qty

            self.total_price += self.products[chosen_item] * \
                self.items[chosen_item]
            self.calculate_discount()
            self.price_to_be_paid = self.total_price - \
                float((self.total_price * self.discount) / 100)

            while True:
                continue_to_shop = input(
                    'Do you want to continue to add items in your shoppin card? (Y or N): ')
                if continue_to_shop not in ['Y', 'N', 'y', 'n']:
                    print('Please write either Y or N')
                    continue
                else:
                    break
            if continue_to_shop.upper() == 'Y':
                continue
            else:
                break

    def __str__(self):
        s = ''
        for key in self.items.keys():
            a = '            '
            a += str(key)
            for i in range(1, 47 - len(a)):
                a += ' '
                i += 1
            a += 'x'
            for i in range(1, 54 - len(a)):
                a += ' '
                i += 1
            a += str(self.items[key])
            for i in range(1, 64 - len(a)):
                a += ' '
                i += 1
            a += '=    €'
            a += str(self.items[key]*self.products[key])
            s += a + '\n'
        print('''
YOUR SHOPPING CART
----------------------------------------------------------------------------
{}
            SUB TOTAL                                          =    €{}
            DISCOUNT                                           =    €{}(%{})
            ----------------------------------------------------------------
            TOTAL                                              =    €{}
        '''.format(s, self.total_price, self.discount_amount, self.discount,  self.price_to_be_paid))


customer1 = Customer('Jack', 'Reacher', 123)

shopping_cart_1 = Items(getattr(customer1, 'customer_id'))
shopping_cart_1.shopping_cart()

customer1.__str__()
shopping_cart_1.__str__()
