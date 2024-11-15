from dataclasses import dataclass
@dataclass 
class animals():
    town: str = ""
    animal: str = ""
    date: str = ""
    walkerAge: int = 0

recordArray = []
with open ("mammals.txt") as file:
    line = file.readline().strip("\n")
    #print(line)
    x = 0
    recordArray = [animals()for i in range(200)]
    while line:
        newRecord = animals()
        items = line.split(",")
        #print(items)
        recordArray[x].town = items[0]
        recordArray[x].animal = items[1]
        recordArray[x].date = items[2]
        recordArray[x].walkerAge = int(items[3])
        #print(recordArray[x])
        x = x + 1
        #recordArray.append(newRecord)
        line = file.readline().strip("\n")
        #print("NEXT LINE:",line)
#print(len(recordArray))
#print("STOP")
#print(recordArray)

def findage(ra):
    #print(ra)
    oldestwalker = ra[0].walkerAge
    for counter in range(200):
        #print("counter - ",counter,"oldest walker",oldestwalker)
        #print("RA Counter Walker Age",ra[counter].walkerAge)
        if ra[counter].walkerAge > oldestwalker:
            oldestwalker = ra[counter].walkerAge
        
    print(oldestwalker)




def displaydates(ra):
    for counter in range(len(ra)):
        #print(ra[counter])
        print(ra[counter].date)



findage(recordArray)
#displaydates(recordArray)