# Create the class Society with following information: society_name, house_no, no_of_members, flat, income
#
# Methods :
#     An __init__ method to assign initial values of society_name, flat, house_no, no_of_members, income
#     input_data() To read information from members allocate_flat() To allocate flat according to income
#     using the below table. show_data() to display the details of the entire class.
#
# Income 	Flat
# >=25000 	A Type
# >=20000 and <25000 	B Type
# >=15000 and <20000 	C Type
# <15000 	D Type

class Society:
    def __init__(self, society_name, flat, house_no, no_of_members, income):
        self.society_name = society_name
        self.flat = flat
        self.house_no = house_no
        self. no_of_members = no_of_members
        self.income = income

    def input_data(self):
        self.society_name = input("Enter Society name: ")
        self.flat = input("Enter flat number: ")
        self.house_no = input("Enter House No: ")
        self.no_of_members = input("Enter No of Members: ")
        self.income = int(input("Enter income: "))

    def allocate_flat(self):
        if self.income >= 25000:
           self.flattype ="A Type"
        elif self.income >= 20000:
             self.flatype = "B Type"
        elif self.income >= 15000:
             self.flattype = "C Type"
        else:
             self.flattype = "D Type"

    def show_data(self):
        return f"Society name: {self.society_name} \tFlat Number: {self.flat}\tHouse number: {self.house_no} " \
               f"\tNo of members: {self.no_of_members} \tFlat type: {self.flattype} \tIncome: {self.income}"


person1 = Society("",0,0,0,0)
person2 = Society("",0,0,0,0)
person3 = Society("",0,0,0,0)


person1.input_data()
person2.input_data()
person3.input_data()

person1.allocate_flat()
person2.allocate_flat()
person3.allocate_flat()

print("  SUMMARY  ".center(100,"-"))
print(person1.show_data())
print(person2.show_data())
print(person3.show_data())


