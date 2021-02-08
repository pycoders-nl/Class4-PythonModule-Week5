'''
RULES FOR TIC-TAC-TOE.
The game is played on a grid that's 3 squares by 3 squares.
You are X, your friend is O. 
The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
When all 9 squares are full, the game is over.
Author= Bulent Caliskan  date= 08/02/2021
'''

class TicTacToe:
    #init functionda 2 oyuncunun isimlerini alip ve oyun panelini ve 
    # kazanmak icin hangi kosullarin olusmasi
    #gerektigini yazioruz.hamle sayisini da 0 yapiyoruz.
    def __init__(self,player1,player2):
        self.player1 = input("Enter your name player 1? ")
        self.player2 = input("Enter your name player 2? ")
        self.panel = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.conditions = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9))
        self.moves = 0

    #Paneli print yapiyoruz
    def createPanel(self):
        print(self.panel[0], self.panel[1], self.panel[2])
        print(self.panel[3], self.panel[4], self.panel[5])
        print(self.panel[6], self.panel[7], self.panel[8])

    #oyuncu 1 in hangi numaraya X koymasini gerektigini soruyoruz.
    #eger sectigi sayida bir isaret (X or O) yoksa isaretliyoruz. moves 1 arttiriyoruz.
    # her seferinde check_win() ile kazandimi diye kontrol ediyoruz.
    #yanli bir numara girerse 1 ole 9 arasinda gir diyoruz.
    def gamer1(self):
            try:
                print(f"{self.player1}")
                place = int(input("Which number would you like to mark {}? \n".format(self.player1)))
                if self.panel[place-1] != "X" and self.panel[place-1] != "O":
                    self.panel[place-1] = "X"
                    self.createPanel()
                    self.moves += 1
                else:
                    print("The other player or you have already taken that row.")
                    self.gamer1()
                self.check_win()
            except :
                print("WRITE A NUMBER FROM 1 TO 9")
                self.gamer1()
    #oyuncu 2 icinde oyuncu 1 ile ayni sartlari yaziyoruz. 
    def gamer2(self):
        try:

            print(f"{self.player2}")
            place = int(input("Which number would you like to mark {}? \n".format(self.player2)))
            if self.panel[place-1] != "X" and self.panel[place-1] != "O":
                self.panel[place-1] = "O"
                self.createPanel()
                self.moves += 1
            else:
                print("The other player or you have already taken that row.")
                self.gamer2()
            self.check_win()
        except:
            print("WRITE A NUMBER FROM 1 TO 9")
            self.gamer2()
    
    #play func.oyuncu 1 ile oyuncu 2 funclarini calistirir.
    def play(self):
        while True:
            self.gamer1()
            self.gamer2()
    #Tekrar oynamak icin oyunculara donusu y/n olan soru soruyoruz.
    #cevap y ise tekrar oaynatiyoruz n ise oyudan cikiyoruz.
    def play_again(self):
        while True:
            question = input("Do you want to play again? Type y or n\n")
            if question == "y":
                self.panel = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                self.run()
            elif question == "n":
                print("See you next time!")
                quit()
            else:
                print("Thats not a valid option")

    #Eger self.conditions daki kosullarin biri olusursa hangi oyuncu once tamamlarsa o kazanir.
    #kazanan belli olduktan sonra tekrar oynamak istermisiniz diye soruyoruz.
    # eger moves 9 olursa yani tum sayilar isaretlenmis olursa oyun biter.
    def check_win(self):
        for i in self.conditions:
            if self.panel[i[0]-1] == self.panel[i[1]-1] == self.panel[i[2]-1] == "X":
                print(f"{self.player1} WINS \nMOVES={self.moves}")
                self.play_again()
            if self.panel[i[0]-1] == self.panel[i[1]-1] == self.panel[i[2]-1] == "O":
                print(f"{self.player2} WINS \nMOVES={self.moves}")
                self.play_again()
            elif self.moves == 9:
                print("GAME OVER")
                exit()            
    
    #oyunun ilk baslangicini olusturmak icin run func kullaniyoruz.
    def run(self):
        self.createPanel()
        self.play()
    
#class i bir object e donuturup.run func. cagiriyoruz.
cos = TicTacToe("","")
cos.run()
