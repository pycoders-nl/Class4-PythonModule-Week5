'''
Create the class Society with following information:
society_name, house_no, no_of_members, flat, income
Methods :
An __init__ method to assign initial values of society_name, flat, house_no, no_of_members, income
input_data() To read information from members
allocate_flat() To allocate flat according to income using the below table.
show_data() to display the details of the entire class.
Income	Flat
>=25000	            A Type
>=20000 and <25000	B Type
>=15000 and <20000	C Type
<15000              D Type
Author= Bulent Caliskan  date= 08/02/2021
'''



class Society:
    def __init__(self,society_name, flat, house_no, no_of_members, income):
        self.society_name = society_name
        self.flat = flat
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.income = income

    def input_data(self):
        self.society_name = input("Enter society name ? ")
        self.house_no = input("Enter your house number ? ")
        self.no_of_members = input("Enter how many members your house has ? ")
        self.income = input("Enter your income ? ")
    
    def allocate_flat(self):
        if self.income >=25000:self.flat="A"
        elif 20000<=self.income<25000:self.flat="B"
        elif 15000<=self.income<20000:self.flat="C"
        else:self.flat="D"
    
    def show_data(self):
        print(f"Your society name       :{self.society_name}\
                   \nYour Flat type          :{self.flat}\
                         \nYour house no           :{self.house_no}\
                              \nYour house no of members:{self.no_of_members}\
                                   \nYour income             :{self.income}")

citizen1=Society("Dark Apt.","D",75,5,26000)
citizen2=Society("Blue Apt.","A",16,4,30000)
  
citizen1.input_data()     
citizen1.show_data() 
citizen2.input_data()     
citizen2.show_data() 