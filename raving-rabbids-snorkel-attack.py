class RavingRabbids():
    def __init__(self,yplayer=0,xplayer=0):
        self.board = [[' ' for a in range(3)] for b in range(7)]
        self.hit = False
        self.yplayer = yplayer
        self.xplayer = xplayer
        self.alive = True
    
    def print_board(self):
        for j in range(len(self.board)):
            print(str(self.board[j]).replace('[','').replace(']','').replace(',',' ||'))
        print()

seconds = -1
scupnum = 25
rabbit1 = RavingRabbids(0,-1)
rabbit2 = RavingRabbids(1,-1)
rabbit3 = RavingRabbids(2,-1)


rabbits = [rabbit1,rabbit2,rabbit3]

        
a = RavingRabbids()

while True:
    for i in rabbits:
        a.board[i.xplayer][i.yplayer] = " "
        if i.alive == False: 
            i.alive = True
            i.xplayer = 0
        else:
            i.xplayer += 1
        
        if i.xplayer > 6:
            print("\nGame over!")
            exit()
        
        if i.hit == True:
            a.board[i.xplayer][i.yplayer] = 'O'
        else:
            a.board[i.xplayer][i.yplayer] = 'X'
    a.print_board()
    seconds +=1
    if seconds == scupnum:
        print("\nYou have survived "+ str(scupnum)+ " seconds! You have won the game!")
        exit()
    if seconds != 1:
        print("You have defended the base for "+str(seconds)+" seconds. "+str(scupnum-seconds)+ " to go until the safe zone is reached!")
    else:
        print("You have defended the base for 1 second. "+ str(scupnum-seconds)+" to go until we're saved!")
    ratnum = int(input("Which colum do you wish to fire: (1,2,3)"))
    for i in rabbits:
        if i.yplayer==(ratnum-1) and i.hit==False: 
            i.hit=True
        elif i.yplayer==(ratnum-1) and i.hit==True:  
            i.alive = False
            i.hit=False
