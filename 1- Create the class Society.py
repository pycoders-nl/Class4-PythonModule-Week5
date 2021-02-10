"""
Create the class Society with following information:

society_name, house_no, no_of_members, flat, income

Methods :
* An __init__ method to assign initial values of society_name, flat, house_no, no_of_members, income.
* input_data() To read information from members.
* allocate_flat() To allocate flat according to income using the below table.
* show_data() to display the details of the entire class.

Income	Flat
>=25000	A Type
>=20000 and <25000	B Type
>=15000 and <20000	C Type
<15000	D Type
"""


class Society:
    """"""
    def __init__(self, society_name='a', house_no='0', no_of_members='0', flat='? Type', income='0'):
        self.society_name = society_name
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.flat = flat
        self.income = income

    def input_data(self, ):
        """read information from members"""
        self.society_name = input("enter society_name: ")
        self.house_no = input("enter house_no: ")
        self.no_of_members = input("enter no_of_members: ")
        self.flat = input("enter flat: ")
        self.income = int(input("enter income: "))

    def allocate_flat(self,):
        """allocate flat according to income"""
        if self.income >= 25000: self.flat = 'A Type'
        elif self.income >= 20000 and self.income < 25000: self.flat = 'B Type'
        elif self.income >= 15000 and self.income < 20000: self.flat = 'C Type'
        elif self.income < 15000: self.flat = 'D Type'

    def show_data(self, ):
        """display the details of the entire class"""
        return print('society_name  : {}\n'
                     'flat          : {}\n'
                     'house_no      : {}\n'
                     'no_of_members : {}\n'
                     'income        : {}\n '
                     .format(self.society_name, self.flat, self.house_no, self.no_of_members, self.income))


"""Test"""

A_society = Society()
A_society.input_data()
A_society.show_data()
A_society.allocate_flat()
A_society.show_data()