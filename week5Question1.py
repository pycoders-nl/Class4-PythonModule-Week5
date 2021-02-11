class Society:
    def __init__(self,society_name, house_no, no_of_members, flat, income):
        self.society_name = society_name
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.flat = flat
        self.income = income
        
    def input_data(self):
        self.society_name = input('Enter society number: ')
        self.house_no = input('Enter house number: ')
        self.no_of_members = input('Enter no of members: ')
        self.income = int(input('Enter income: '))

    def allacote_flat(self):
        if self.income < 15000:
            self.flat = 'D Type'
        elif 15000 <= self.income <= 20000:
            self.flat = 'C Type'
        elif 20000 <= self.income <= 25000:
            self.flat = 'B Type'
        elif self.income >= 25000:
            self.flat = 'A Type'

    def show_data(self):
        return ('Society name:', self.society_name, 'House number:',self.house_no,'No of members:',self.no_of_members,'Flat type:',self.flat,'Income:',self.income)

a = Society("First","A type", 11, 5, 27000)
b = Society("Second",'B Type', 22,112,2000)
c = Society("Third",'C Type',33, 43, 16000)
d = Society("Fourth","D Type", 44, 54, 5000)

#a.input_data()
# b.input_data()
# c.input_data()
a.allacote_flat()
# b.allacote_flat()
# c.allacote_flat()
print(a.show_data())
# print(b.show_data())
# print(c.show_data())
