count = 0
game_over =False

class AngryBirds():
    def __init__(self):
        self.board = [[' ' for a in range(3)] for b in range(3)]
        self.xplayer = 0
        self.yplayer = 2
    
    def board_positions(self):
        self.board[1][1] = 'T'
        self.board[2][2] = 'S'
        self.board[self.yplayer][self.xplayer] = 'B'

    def printboard(self):
        self.board_positions()
        for i in range(len(self.board)):
            print(self.board[i])
    
    def board_movement(self):
        no_movements = int(input("Please enter number of movements"))
        while count < no_movements:
            new_player_pos = str(input("u,d,l,r"))
            if new_player_pos == "u":
                if self.yplayer < 1:
                    self.board[self.yplayer][self.xplayer] = "B"
                    for i in self.board:
                        print(i)
                    print("Out of bounds 1")
                    print("Try again")
                else:
                    self.board[self.yplayer][self.xplayer] = " "
                    self.yplayer -= 1
                    self.board[self.yplayer][self.xplayer] = "B"
                    for i in self.board:
                        print(i)
            elif new_player_pos == "r":
                if self.xplayer < 1:
                    self.board[self.yplayer][self.xplayer] = "B"
                    for i in self.board:
                        print(i)
                    print("Out of bounds")
                    print("Try again")
                else:
                    self.board[self.yplayer][self.xplayer] = " "
                    self.xplayer -= 1
                    self.board[self.yplayer][self.xplayer] = "B"
                    for i in self.board:
                        print(i)
            elif new_player_pos == "d":
                if self.yplayer > 1:
                    self.board[self.yplayer][self.xplayer] = "B"
                    for i in self.board:
                        print(i)
                    print("Out of bounds 3")
                    print("Try again")
                else:
                    self.board[self.yplayer][self.xplayer] = " "
                    self.yplayer += 1
                    self.board[self.yplayer][self.xplayer] = "B"
                    for i in self.board:
                        print(i)
            elif new_player_pos == "l":
                if self.xplayer < 1:
                    self.board[self.yplayer][self.xplayer] = "B"
                    for i in self.board:
                        print(i)
                    print("Out of bounds 4")
                    print("Try again")
                else:
                    self.board[self.yplayer][self.xplayer] = " "
                    self.xplayer -= 1
                    self.board[self.yplayer][self.xplayer] = "B"
                    for i in self.board:
                        print(i)
       

a = AngryBirds()
a.printboard()
a.board_movement()
