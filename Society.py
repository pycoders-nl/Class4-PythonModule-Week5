

class Society:
    def __init__(self, society_name, house_no, no_of_members, flat, income):
        # constructor
        self.society_name = society_name
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.flat = flat
        self.income = income

    def input_data(self):

        self.society_name = input("Enter Society Name:")
        self.house_no = input("Enter House Number")
        self.no_of_members = input("Enter No.of members")
        self.income = int(input("Enter income"))

    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = "A Type"
        elif self.income >= 20000 and self.income < 25000:
            self.flat = "B Type"
        elif 15_000 <= self.income < 20_000:
            self.flat = "C Type"
        else:
            self.flat = "DType"

    def show_data(self):

        return f"Society name: {self.society_name} \tHouse number: {self.house_no} \tNo of members: {self.no_of_members} \tFlat type: {self.flat} \tIncome: {self.income}"


s1 = Society("Dream Apartments",  16, 3, "D type", 18000) # Member S1
s1.allocate_flat()
print(s1.show_data())