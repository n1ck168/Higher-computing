
def enterweightoffood():
    totalWeight = 0
    for counter in range (5):
        foodweight = int(input("Please enter the size of each portion in grams"))
        while foodweight < 0 or foodweight > 200:
            print("This is an invalid amount, each container can only hold a maximum of 200g")
            foodweight = int(input("Please re-enter a valid weight in grams"))
        containerweights.append(foodweight)
        totalWeight = totalWeight + foodweight
    return totalWeight

def entersizeofdog():
    dogsize = input("Please enter your dogsize: small, medium, or large")
    return dogsize
    
def storemessage(dogsize, totalweight):
    if dogsize == small and totalweight > 110 and totalweight < 140:
        print("This weight is suitable for your small dog")
    elif dogsize == medium and totalweight > 330 and totalweight < 440:
        print("This weight is suitable for your medium dog")
    elif dogsize == large and totalweight > 690 and totalweight < 900:
        print("This weight is suitable for your large dog")
    else:
        print("This portion size is invalid")

def calcavgweight(totalWeight):
    averageweight = totalWeight / 5
    averageweight = round(averageweight,1)
    return averageweight
def displayoutputmessage(aw, totalWeight):
    for i in range (5):
        print(containerweights[i])
    print(totalWeight)
    print(aw)



containerweights = []
small = range(110,140)
medium = range(330,440)
large = range(690,900)
#1. Enter valid weight of food in each container and calculate total weight
tW = enterweightoffood()
#2. Enter size of dog
ds = entersizeofdog()
#3. Store a message that states if the total weight of food is within the recommended range for the size of dog entered
storemessage(ds, tW)
#4. Calculate average weight of food
aw = calcavgweight(tW)
#5. Display output messages 
displayoutputmessage(aw,tW)