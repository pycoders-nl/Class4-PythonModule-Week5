class Society:
    def __init__(self, society_name='', flat='', house_no=0, no_of_members=0, income=0):
        self.society_name = society_name
        self.income = income
        self.house_no = house_no
        self.flat = self.allocate_flat()
        self.no_of_members = no_of_members

    def input_data(self):
        self.society_name = input('Enter the Society Name.............: ')
        self.house_no = int(input('Enter the House Number.............: '))
        self.no_of_members = int(input('Enter the Number of Members........: '))
        self.income = int(input('Enter the Income...................: '))
        self.flat = self.allocate_flat()
    def allocate_flat(self):
        if self.income >= 25000:
            return 'A Type'
        elif 20000 <= self.income < 25000:
            return 'B Type'
        elif 15000 <= self.income < 20000:
            return 'C Type'
        else:
            return 'D Type'

    def show_data(self):
        s = '\n'.join(['Society Name is ' + self.society_name, '\nFlat Type is ' + self.flat,
                       '\nHouse Number is ' + str(self.house_no), '\nNumber of Members is ' + str(self.no_of_members),
                       '\nIncome is ' + str(self.income)])
        return s


s1 = Society()
s1.input_data()
print(s1.show_data())