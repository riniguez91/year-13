import datetime
import time
class Train:
    def __init__(self):
        self.destinations=[["12:19","Asnee"],["13:27","Ratnum"],["15:00","Usna"],["14:10","Scoopnum"],["16:00","Big Shaq"],["22:00","MCNBH"]]
       
    def print_table(self):
        skrra = datetime.datetime.now()
        now = skrra.strftime("%H:%M")
        print(now)
        for i in self.destinations:
            if skrra.time() < datetime.time(hour=int(i[0].split(":")[0]), minute=int(i[0].split(":")[1])):
                if i[0].split(":")[0] == now.split(":")[0]:
                    if int(i[1].split(":")[0]) - int(now.split(":")[0]) < 4:
                        print(i, " destination incoming")
                else:
                    print(i)
            else:
                print("No available trains")
                break
a = Train()
count = 0
while True:
    a.print_table()
    time.sleep(1)
    count += 1 
    if count == 30:
        j = str(input("Would you like to exit?"))
        if j == "Yes":
            exit()
        
