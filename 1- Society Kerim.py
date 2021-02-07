# Question 1:
# Create the class Society with following information:

# society_name, house_no, no_of_members, flat, income

# Methods :

# An __init__ method to assign initial values of society_name, flat, house_no, no_of_members, income
# input_data() To read information from members
# allocate_flat() To allocate flat according to income using the below table.
# show_data() to display the details of the entire class.

class Society:
    def __init__(self, society_name, flat, house_no, no_of_members, income): # __init__ method
        self.society_name = society_name
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.flat = flat
        self.income = income

    def input_data(self):
        """ Reads information from members """
        self.society_name = input("Enter society name: ")
        self.house_no = input("Enter house number: ")
        self.no_of_members = input("Enter no of members: ")
        self.income= int(input("Enter income: "))


    def allocate_flat(self):
        """ Allocates flat according to income using the below table. """
        if self.income >= 25_000:
            self.flat = "A Type"
        elif 20_000 <= self.income < 25_000:
            self.flat = "B Type"
        elif 15_000 <= self.income < 20_000:
            self.flat = "C Type"
        elif self.income < 15_000:
            self.flat = "D Type"


    def show_data(self):
        """ Displays the details of the entire class. """
        return f"Society name: {self.society_name} \tHouse number: {self.house_no} \tNo of members: {self.no_of_members} \tFlat type: {self.flat} \tIncome: {self.income}"

s1 = Society("Top Apartments", "A type", 36, 4, 26_000) # Member S1 
s2 = Society("Best Apartments", "C type", 24, 9, 21_000) # Changes Flat type as "B type"
s3 = Society("Poor Apartments", "B type", 12, 16, 6_000) # Changes Flat type as "D type"
#s1.input_data()
#s2.input_data()
#s2.input_data()
s1.allocate_flat()
s2.allocate_flat()
s3.allocate_flat()
print(s1.show_data())
print(s2.show_data())
print(s3.show_data())

