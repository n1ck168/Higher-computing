print("These are the recommended daily portions for your dog: \n- Small = 110g to 140g\n- Medium = 330g to 440g\n- Large = 690g to 900g")
weightperportion = int(input("Please enter a valid weight for each portion in grams"))
totalweight = weightperportion * 5
dogSize = input("Please enter the size of your dog")

small = range(110,140)
medium = range(330,440)
large = range(690,900)

while dogSize == small:
    if totalweight < 110 or totalweight > 140:
        print("You have entered an invalid portion for your size of dog")
        weightperportion = int(input("PLease enter a valid weight for each portion in grams"))
        totalweight = weightperportion * 5
    print("You have entered a valid portion size")
