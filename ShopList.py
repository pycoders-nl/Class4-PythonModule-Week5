

class Customer():
    def __init__(self):
        self.cust_name = ""
        self.Cust_Surname = ""
        #self.full_name = ""


    def get_cust_info(self):
        self.cust_name = input("Enter Your Name:")
        self.Cust_Surname = input("Enter Your Surname")
        self.full_name= self.cust_name + " " + self.Cust_Surname
        self.Cust_id = Customer_No_list.get(self.full_name)


    def showAll(self):
        print (f"Sayin {self.Cust_id} {self.full_name} aliverise baslayabilirsiniz, urun ve miktarini seciniz:")
        print  (f"Urun ve Fiyat Listesi: kitap:100, kalem:50, silgi: 50, defter: 200")
        return

Customer_No_list= { "metin tanca": 12346, "mahir canata": 12345 }  #girilen isim onceden kayitli mi, musteri nosu nedir bakiyoruz
customer1 = Customer()
customer1.get_cust_info()
print (customer1.showAll())

class Items(Customer):
    def __init__(self, Cust_name ):
        self.Cust_name= Cust_name
        self.product =["kitap", "kalem", "silgi", "defter"]
        self.price = """{"kitap":100, "kalem":50,"silgi": 50,"defter": 200}"""
        self.total_price=0
        self.price_tobe_paid=0
        self.alinan_urun = 0
        self.alinan_urunler=[]
        self.alinan_miktarlar=[]
        self.qty = 0
        self.total_discount=0

    def __str__(self):
        print(f"musteri kodu:{self.Cust_name} ve urun fiyatlari : {self.price}")

    def calculate_discount(self):
        self.total_price= self.price * self.qty
        if self.total_price >= 4000:
            self.discount=0.25
        elif self.total_price >= 2000:
            self.discount=0.15
        elif self.total_price < 2000:
            self.discount=0.1
        return self.discount

    def shopping_cart(self):

        self.alinan_urun=input("kirtasiye urununu giriniz: ")
        self.price=int(input("fiyatini giriniz? "))
        self.qty=int(input("miktarini giriniz: "))

        return self.alinan_urun, self.qty

    def get_total_amount(self):
        self.price_tobe_paid = self.total_price*(1-self.discount)
        self.total_discount=self.total_price*self.discount
        return (f"toplam odenen:{self.price_tobe_paid} toplam indirim:{self.total_discount}")


    def __str__(self):
        return f"Alinan urunler {self.alinan_urun} ve toplam odenen {self.price_tobe_paid} ve toplam indirim {self.total_discount}"

a=Items(Customer)
a.shopping_cart()
a.calculate_discount()
a.get_total_amount()
# print(a.price_tobe_paid)
print(a.__str__())