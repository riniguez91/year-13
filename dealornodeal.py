import random

class Cards:
    def __init__(self):
        self.prizes = [0.01,0.1,0.5,1,5,10,50,100,250,500,750,1000,3000,5000,10000,15000,20000,35000,50000,75000,100000,250000]
        self.prizes2 = [0.01,0.1,0.5,1,5,10,50,100,250,500,750,1000,3000,5000,10000,15000,20000,35000,50000,75000,100000,250000]
        self.boxes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
        self.gameover = False
        self.ratnum = 0 
        self.sku = 0 
    
    def display_money(self):
        print("Amount of money that hasn't been opened")
        for i in self.prizes2:
            print(i,end='|')
        print()
    
    def final_choice(self,box):
        print("ONLY 2 BOXES REMAAIN!\nYou can either keep your box or swap it\nDecide wisely!")
        fc = ''
        while fc != 'k' or fc != 's':
            fc = str(input("Keep(k) or swap(s)\n"))
            if fc == 'k':
                print("Your box contains: " + self.prizes2[box-1])
            else:
                print("You swap your box and it contains " + self.prizes2[box-1])
            self.gameover = True
    
    def banker(self,box):
        offer = self.prizes2[box-1]*0.6
        choice = False
        while choice == False:
            skrra = str(input("Accept offer? y/n\n"))
            if skrra == 'y':
                choice = True
                self.gameover = True
                print("You won £"+str(offer))
            else:
                choice = True
        
    def game(self,box):
        random.shuffle(self.prizes2)
        self.boxes.remove(box)
        print("Your lucky box number is " + str(box))
        while self.gameover == False:
            self.display_money()
            print("You can open the following boxes:")
            for i in range(len(self.boxes)):
                print(self.boxes[i],end='|')
            boxToOpen = int(input("\nChoose your box fella(1-22)"))
            if boxToOpen in self.boxes:
                self.boxes.remove(boxToOpen)
                print("The box opened contains: " +str(self.prizes[boxToOpen]))
                self.prizes2.remove(self.prizes[boxToOpen-1])
                if len(self.boxes) <= 16 and len(self.boxes)%3==1:
                    self.banker(box)
            else:
                print("Sike!You can't open that box my dude")
            if len(self.prizes2)==1:
                self.final_choice(box)
    
    def start(self):
        self.ratnum = random.randint(0,21)
        self.sku = self.ratnum +1
        a.game(self.sku)
        
a = Cards()
a.start()
