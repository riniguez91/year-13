class SupermarketSweep():
    def __init__(self):
        self.board = [[" " for a in range(7)] for b in range(4)]
    
    def board_positions(self):
        self.board[1][1] = 'F'
        self.board[2][1] = 'F'
        self.board[1][3] = 'V'
        self.board[2][3] = 'V'
        self.board[1][5] = 'D'
        self.board[2][5] = 'D'

    def printboard(self):
        self.board_positions()
        for i in range(len(self.board)):
            print(self.board[i])
    
class ProductSweep():
    def __init__(self,question,answer,options):
        self.question = question 
        self.answer = answer
        self.options = options
    
    def ask(self):
        return self.question
    

a = ProductSweep("The monkey loves to eat me , im a: _ _ _ _ _", 'banana','F')
b = ProductSweep("I'm always used in saladas + i'm green:  _ _ _ _ _", 'lettuce','V')
c = ProductSweep("Without me there would be no life: _ _ _ _ _ _",'water','D')
d = ProductSweep("Im fizzy and was used as a medicine in wars: _ _ _ _ _ _ ",'coca-cola','D')
e = ProductSweep("I gave birth to one of the most famous laws: _ _ _ _ _ ",'apple','F')
questions = [a,b,c,d,e]
supermarket=SupermarketSweep()

lifes = 3
correct = 0
for j in questions:
    supermarket.printboard()
    print(j.ask())
    u = input()
    if u == j.answer:
        print("CORRECT")
        if input("Which section? ") == j.options:
            print("Correct!")
            correct += 1
            if correct ==3:
                print("You have won the game and netted 2000 euros!")
        else:
            print("INCORRECT, you have lost the game")
            break
    else:
        lifes -= 1
        if lifes == 0:
            print("Game over, you have " +str(lifes) +" lifes left")
            break
        print("Incorrect, you have " +str(lifes) +" lifes left")
