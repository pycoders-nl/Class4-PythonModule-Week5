class Society:
    def __init__(self):
        self.society_name = ''
        self.house_no = 0
        self.no_of_members = 0
        self.flat = '' 
        self.income = 0

        self.input_data()
        self.allocate_flat()
        self.show_data()

    def input_data(self):
        self.society_name = input("Society name girin: ")
        self.house_no = input("House no girin: ")
        self.no_of_members = int(input("No of members: "))
        self.income = int(input("Income: "))

    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = 'A Type'
        elif self.income >= 20000:
            self.flat = 'B Type'
        elif self.income >= 15000:
            self.flat = 'C Type'
        else:
            self.flat = 'D Type'
        

    def show_data(self):
        print(f"""
        Society name: {self.society_name}
        House no: {self.house_no}
        No of members: {self.no_of_members}
        Flat: {self.flat}
        Income: {self.income}
        """)

s = Society()

