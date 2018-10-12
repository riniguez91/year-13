import random
import time

class BigBreak():
    def __init__(self):
        self.pot = 0
        self.lifes = 3
        self.balls = ['Black']
        self.questions1 = [['What is the chance of raining today?',0.5],['What is the chance of snowing?',0.3],['What is the chance of there being a cloudy day?',0.2],['What is the chance of there being a clear sky?',0.8],['What is the chance of there being a humid day?',0.1],['What is the chance of anything happening at all today?',1]]
        self.questions3 = ['Who is the author of the song "Mans not hot"','Big Shaq']
        self.questions4 = ['What is the capital of France?','Paris']
        self.questions5 = ['What is the last name of the former US president Barack?','Obama']
        self.questions6 = ['Which club bought Neymar for the highest transfer fee?','PSG']
        self.questions7 = ['What is the screen resolution of most laptops?','1366x780']
    
    def printBalls(self):
        print("\nThe following balls are left: " + str(self.balls).replace('[','').replace(']','').replace(',','').replace("'",'') + "\nNote you must hit them in the following order: 1)Yellow 2)Green 3)Brown 4)Blue 5)Pink 6)Black")
    
    def checkStatistacks(self):
        if len(self.balls)!=0:
            hit = self.balls[random.randint(0,len(self.balls)-1)]
        if (self.lifes != 0) or (len(self.balls)!=1):
            if 'Red' in self.balls:
                if hit != 'Red':
                    print("\nYou hit ball other than a red ball, prepare for the question!")
                    hit2 = random.randint(0,len(self.questions1)-1)
                    print(self.questions1[hit2-1][0])
                    answer = float(input("Please enter here: "))
                    if answer == self.questions1[hit2-1][1]:
                        print("Correct! You have earned 10 pounds!")
                        self.pot += 10
                    else:
                        self.lifes -= 1
                        print("Wrong your current lifes are: ",str(self.lifes))
                    #self.questions1.remove(self.questions1[hit2])
                else:
                    print("\nYou hit a red ball!")
                    time.sleep(1)
                    self.balls.remove(hit)
            else:
                a.printBalls()
                if self.balls.index(hit) > 0:
                    print("\nYou hit the ball in the wrong order, prepare for question time!")
                    if (self.balls.index(hit)-1) == 0: 
                        print(self.questions3[0])
                        answer = input("Please enter here: ")
                        if answer == str(self.questions3[1]).replace("'",''):
                            print("Correct! You have earned 30 pounds!")
                        else:
                            self.lifes -= 1 
                            print("Wrong your current lifes are: ",str(self.lifes))
                    elif (self.balls.index(hit)-2) == 0:
                        print(self.questions4[0])
                        answer = input("Please enter here: ")
                        if answer == str(self.questions4[1]).replace("'",''):
                            print("Correct! You have earned 40 pounds!")
                        else:
                            self.lifes -= 1 
                            print("Wrong your current lifes are: ",str(self.lifes))
                    elif (self.balls.index(hit)-3) == 0:
                        print(self.questions5[0])
                        answer = input("Please enter here: ")
                        if answer == str(self.questions5[1]).replace("'",''):
                            print("Correct! You have earned 50 pounds!")
                        else:
                            self.lifes -= 1 
                            print("Wrong your current lifes are: ",str(self.lifes))
                    elif (self.balls.index(hit)-4) == 0:
                        print(self.questions6[0])
                        answer = input("Please enter here: ")
                        if answer == str(self.questions6[1]).replace("'",''):
                            print("Correct! You have earned 60 pounds!")
                        else:
                            self.lifes -= 1 
                            print("Wrong your current lifes are: ",str(self.lifes))
                    elif (self.balls.index(hit)-5) == 0:
                        print(self.questions7[0])
                        answer = input("Please enter here: ")
                        if answer == str(self.questions7[1]).replace("'",''):
                            print("Correct! You have earned 70 pounds!")
                        else:
                            self.lifes -= 1 
                            print("Wrong your current lifes are: ",str(self.lifes))
                else:
                    if hit == 'Yellow':
                        print("\nYou hit them in the correct order!")
                        self.pot += 20
                        self.balls.remove(hit)
                    elif hit == 'Green':
                        print("\nYou hit them in the correct oder!")
                        self.pot += 30 
                        self.balls.remove(hit)
                    elif hit == 'Brown':
                        print("\nYou hit them in the correct order!")
                        self.pot += 40
                        self.balls.remove(hit)
                    elif hit == 'Blue':
                        print("\nYou hit them in the correct order!")
                        self.pot += 50
                        self.balls.remove(hit)
                    elif hit == 'Pink':
                        print("\nYou hit them in the correct order!")
                        self.pot += 60 
                        self.balls.remove(hit)
                    else:
                        print("\nYou hit them in the correct order!")
                        self.pot += 70
        else:
            print("\nGame over! You won: £",str(self.pot))
            exit()
            
        
a = BigBreak()
while True:
    a.checkStatistacks()
        
