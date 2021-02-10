import random
from tabulate import tabulate
house_numbers = list(range(1, 101))


class Society:
    def __init__(self):
        self.society_name = None
        self.flat = None
        self.house_no = 0
        self.no_of_members = 0
        self.income = 0

    def input_data(self):
        self.no_of_members = int(
            input("how many people will live in the house ?: "))
        for i in range(0, self.no_of_members):
            self.income += int(input("how much is the income of person %d ?: " % (i+1)))

    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = "A Type"
            self.society_name = "Riches"
            self.house_no = random.choice(house_numbers[0:26])
            house_numbers.remove(self.house_no)
        elif self.income >= 20000:
            self.flat = "B Type"
            self.society_name = "Middle Incomes"
            self.house_no = random.choice(house_numbers[26:51])
            house_numbers.remove(self.house_no)
        elif self.income >= 15000:
            self.flat = "C Type"
            self.society_name = "Low Incomes"
            self.house_no = random.choice(house_numbers[51:76])
            house_numbers.remove(self.house_no)
        else:
            self.flat = "D Type"
            self.society_name = "Poors"
            self.house_no = random.choice(house_numbers[76:])
            house_numbers.remove(self.house_no)

    def show_data(self):
        print(tabulate([[self.society_name, self.flat,
                         self.house_no, self.income, self.no_of_members]], headers=["Society Name", "Flat", "House No", "Income", "Number of Members"]))


society = Society()
society.input_data()
society.allocate_flat()
society.show_data()
