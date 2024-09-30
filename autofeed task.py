totalweight = 0 
containerweights = []
small = range(110,140)
medium = range(330,440)
large = range(690,900)
for counter in range (5):
    foodweight = int(input("Please enter the size of each portion in grams"))
    while foodweight < 0 or foodweight > 200:
        print("This is an invalid amount, each container can only hold a maximum of 200g")
        foodweight = int(input("Please re-enter a valid weight in grams"))
    containerweights.append(foodweight)
    totalWeight = totalweight + foodweight

dogsize = input("Please enter your dogsize: small, medium, or large")

if dogsize == small and totalweight > 110 and totalweight < 140:
    weightmessage = print("This weight is suitable for your small dog")
elif dogsize == medium and totalweight > 330 and totalweight < 440:
    weightmessage = print("This weight is suitable for your medium dog")
elif dogsize == large and totalweight > 690 and totalweight < 900:
    weightmessage = print("This weight is suitable for your large dog")
else:
    weightmessage = print("This portion size is invalid")

averageweight = totalweight / 5
averageweight = round(totalweight,1)

for i in range (5):
    print(containerweights[i])
print(totalweight)
print(averageweight)
print(weightmessage)
