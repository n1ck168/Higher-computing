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
    print(line)
    while line:
        newRecord = animals()
        items = line.split(",")
        #print(items)
        newRecord.town = items[0]
        newRecord.animal = items[1]
        newRecord.date = items[2]
        newRecord.walkerAge = int(items[3])
        recordArray.append(newRecord)
        line = file.readline().strip("\n")
        print("NEXT LINE:",line)

print("STOP")
print(recordArray)

def findage(ra):
    oldestwalker = ra[0].walkerAge
    for counter in range(len(ra)):
        if ra[counter].walkerAge > oldestwalker:
            ra[counter] = oldestwalker
        counter = counter + 1
    print(oldestwalker)
findage(recordArray)



def displaydates(ra):
    for i in range(len(ra)):
        print(ra[i].date)
        i = i + 1

displaydates(recordArray)