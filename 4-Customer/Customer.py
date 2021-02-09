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