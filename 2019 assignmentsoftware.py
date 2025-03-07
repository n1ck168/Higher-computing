from dataclasses import dataclass
@dataclass 
class member():
    forename: str = ""
    surname: str = ""
    distance: float = 0.0

recordArray = []
with open ("members.txt") as file:
    line = file.readline().strip("\n")
    #print(line)
    x = 0
    recordArray = [member() for i in range ]
    while line:
        newRecord = member()
        items = line.split(",")
        #print(items)
        recordArray[x].forename = items[0]
        recordArray[x].surname = items[1]
        recordArray[x].distance = int(items[2])
        
        print(recordArray[x])
        x = x + 1
        recordArray.append(newRecord)
        line = file.readline().strip("\n")