import random #14/10 23.14

class Player:
    def __init__(self, name, total=0, played=False):
        self.name = name
        self.total = total
        self.played = played

class Question:
    def __init__(self, question, correct):
        self.question = question
        self.correct = correct

class Game:
    def begin(self, playerA, playerB):
      global totalGames
      while True:
        if totalGames == 2:
          print("GAME OVER!")
          break
        if totalGames == 1 and playerA.played == 4:
          break
        if totalGames == 1 and playerB.played == 4:
          break
        if playerA.played == True:
          self.highOrLow(playerB)
        if playerB.played == True:
          self.highOrLow(playerA)

    def test(self,playerA, playerB):
      global testStatus
      while testStatus == True:
        global totalGames
        print(totalGames)
        if totalGames == 2:
          break
        qChoice = random.randint(1,len(qList))
        print(qList[qChoice-1].question)
        AAnswer = int(input("{}, please enter your estimation".format(playerA.name)))
        BAnswer = int(input("{}, please enter your estimation".format(playerB.name)))
        if qList[qChoice-1].correct > AAnswer:
          Adifference = qList[qChoice-1].correct - AAnswer
        elif qList[qChoice-1].correct < AAnswer:
          Adifference = AAnswer - qList[qChoice-1].correct
        else:
          Adifference = 0
        if qList[qChoice-1].correct > BAnswer:
          Bdifference = qList[qChoice-1].correct - BAnswer
        elif qList[qChoice-1].correct < BAnswer:
          Bdifference = BAnswer - qList[qChoice-1].correct
        else:
          Bdifference = 0
        print(qList[qChoice-1].correct)
        print(playerA.name," was ",Adifference," away!")
        print(playerB.name," was ",Bdifference," away!")
        if Adifference < Bdifference:
          print(playerA.name, " wins!")
          testStatus = False
          self.highOrLow(player1)
        elif Adifference > Bdifference:
          print(playerB.name, " wins!")
          testStatus = False
          self.highOrLow(player2)
        else:
          del qList[qChoice-1]
    
    def highOrLow(self, person):
      while cardSets != []:
        global totalGames
        totalGames += 1
        cards = cardSets.pop()
        print("The first card is ",cards[0])
        print("Welcome", person.name)
        for j in range(1,length):
          print("")
          print("Higher or lower? (TYPE 'h' or 'l'): ")
          choice = input()
          if choice == "h":
            print("The next card is: ", cards[j])
            print("")
            if value.get(cards[j]) > value.get(cards[j-1]):
              print("Well done")
              person.total+=1
              print("{}, has {} points".format(person.name,person.total))
            else:
              print("Bad luck")
              print("{}, finished with {} point(s)".format(person.name,person.total))
              person.played = True
              return "Game Over"
            if person.total == 4:
              return "Player wins"
          elif choice == "l":
            print("The next card is: ", cards[j])
            print("")
            if value.get(cards[j]) < value.get(cards[j-1]):
              print("Well done")
              person.total+=1
              print("{}, has {} points".format(person.name,person.total))
            else:
              print("Bad luck")
              print("{}, finished with {} point(s)".format(person.name,person.total))
              person.played = True
              return "Game Over"
            if person.total == 4:
              return "Player wins"

deck = list('23456789JQKA'*4)
deck.append("10")
deck.append("10")
deck.append("10")
deck.append("10")
random.shuffle(deck)
value = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
          '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
p1cards = [deck.pop() for _ in range(5)]
p2cards = [deck.pop() for _ in range(5)]
cardSets = [p1cards,p2cards]
length = len(p1cards)

#checks the set of cards for each player
for i in range(1,length):
  for j in range(1,length):#changed from j-1
    if p1cards[j] == p1cards[j-1]:
      p1cards.pop(j)
      newCard = deck.pop()
      p1cards.insert(j,newCard)
#now for player 2's set
for i in range(1,length):
  for j in range(1,length):#changed from j-1
    if p2cards[j] == p2cards[j-1]:
      p2cards.pop(j)
      newCard = deck.pop()
      p2cards.insert(j,newCard)

global totalGames
totalGames = 0
global testStatus
testStatus = True
Q1 = Question("How many fingers do we have?", 8)
Q2 = Question("How many tracks are there in Mario Kart 64?",16)
qList =[Q1,Q2]
player1 = Player("James",0,False)
player2 = Player("Gavin",0,False)
pList = [player1,player2]
game=Game()
game.test(player1,player2)
game.begin(player1,player2)
print("{}, had {}, and {}, had {}".format(player1.name,player1.total,player2.name,player2.total))
