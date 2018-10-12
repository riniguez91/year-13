import random

class WiiPartySwapMeet():
    def __init__(self):
        self.board = [[],[],[],[]]
        self.colours = ['Y','B','O','G','W','P']
        self.options = ['B','Y','O','W']
        self.player = 0
    
    def create_board(self):
        for i in range(4):
            for j in range(6):
                self.board[i].append(self.colours[random.randint(0,5)])
        #print(str(self.board).replace('[','').replace(']','').replace(',',''))
        
    def print_board(self):    
        for index,k in enumerate(self.board):
            print("Player " + str(index+1) + ": " + str(k).replace('[','').replace(']','').replace(',','').replace("'",''))
        print()
    
    def append_options(self,player):
        print("Player " + str(player+1) + " turn now")
        print("This are the available options: " + str(self.options).replace('[','').replace(']','').replace("'",'').replace(",",""))
        asnee=int(input("Select from 1 to 6 a character to replace, please note it is not as an array so the first element is one."))
        ratnum=int(input("Swap " + self.board[player][asnee-1] + " with " + str(self.options).replace('[','').replace(']','').replace("'",'').replace(",","") + "; please put a number: "))
        self.board[player][asnee-1] = self.options[ratnum-1]
        self.options.remove(self.options[ratnum-1])
        if len(self.options) == 0:
            for y in range(4):
                self.options.append(self.colours[random.randint(0,5)])
        if self.board[player][0] == self.board[player][1] and self.board[player][1] == self.board[player][2] and self.board[player][2] == self.board[player][3] and self.board[player][3] == self.board[player][4] and self.board[player][4] == self.board[player][5]:
	        print("You won the game!")
	        exit()

    
a = WiiPartySwapMeet()
a.create_board()
while True:
    for i in range(4):
        a.print_board()
        a.append_options(i)
    
    
