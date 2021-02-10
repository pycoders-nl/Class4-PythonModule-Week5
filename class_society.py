class Society:
    def __init__(self,society_name, house_no, no_of_members, flat, income):
        self.society_name=society_name
        self.house_no=house_no
        self.no_of_members=no_of_members
        self.flat=flat
        self.income=income

    def input_data(self):
        self.society_name=input("society_name'i giriniz")
        self.house_no=input("house_no'u giriniz")
        self.no_of_members=input("no_of_members 'ı giriniz")
        self.flat=input("flat'ı giriniz")
        self.income=int(input("income'i giriniz"))
    def allacote_flat(self):
        if self.income >=25000:
           self.flat="A Type"
        elif self.income>=20000 and self.income<25000:
            self.flat="B Type"
        elif self.income>=15000 and self.income<20000:
            self.flat="C Type"
        elif self.income<15000:
            self.flat="D Type"


    def show_data(self):
        """print(self.society_name, self.house_no, self.no_of_members, self.flat, self.income)"""


        return f"society_name:{self.society_name}\thouse_no:{self.house_no}\tno_of_members:{self.no_of_members}\tflat:{self.flat}\tincome:{self.income}."

a=Society("street",5,6,4,2)

print(a.input_data())
print(a.allacote_flat())
print(a.show_data())