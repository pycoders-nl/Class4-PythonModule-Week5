class society:
    def __init__(self, society_name, house_no, no_of_members, income):
        self.society_name = society_name
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.income = income
        self.allocate_flat()

    def inputdata(self):
        self.society_name = input("Enter Society Name:")
        self.house_no = input("Enter House Number:")
        self.no_of_members = input("Enter No of members:")
        self.income = float(input("Enter income:"))
        self.allocate_flat()

    def complete(self):
        return f"society_name: {self.society_name} house_no: {self.house_no} no_of_members: " \
               f"{self.no_of_members} income: {self.income} flat type: {self.flat} "

    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = "AType"

        elif 20000 <= self.income < 25000:
            self.flat = "BType"

        elif 15000 <= self.income < 20000:
            self.flat = "CType"

        else:
            self.flat = "DType"

    def showdata(self):
        print("Society Name", self.society_name)
        print("House_No", self.house_no)
        print("No.of members", self.no_of_members)
        print("Flat Type", self.flat)
        print("Income", self.income)


S = society("a", "b", "c", 10000)

S.showdata()

print(S.complete())

