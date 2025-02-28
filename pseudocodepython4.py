#Challenge 4 - Number of tin cans in a pack

#At the local PackingTins4U factory, tin cans are usually packed in squares of size x by x cans for efficiency with just one can high.
#However, if x is a single digit, then sometimes the factory runs a special offer by adding a certain number of additional rows of cans for free to make a rectangle pack of dimensions x + a cans along by x cans wide.
#First input x, the length of the square packs being made.
#If and only if relevant, also input whether a special offer is running which will be indicated by a y for special offer and n for no special offer.
#If and only if it is a special offer, also input a, the number of additional rows which are being included for free. This input will only be available if there is a special offer running.
#Output the number of tin cans that each pack will contain.

#Pseudocode
#Ask for and store x (length of square packets being made)
#If x is a single digit then
#     Ask for and store a special offer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
#    If y then
#        Ask for and store the number of additional rows included for free
#Calculate numberoffreerows
#Output numberoftincans

def getValidSpecialOffer():
#     3.1. Ask for and store _______________
# 3.2. While ____________ and _______________ Do
# 3.3.       Output error message
# 3.4.       Ask for and store _____________
# 3.5. End While
    specialOffer = input("Is there a special offer? (y/n): ")
    while specialOffer.lower() != "y" and specialOffer.lower() != "n":
        print("Error. Only enter y or n.")
        specialOffer = input("Is there a special offer? (y/n): ")
    return specialOffer.lower()

x = int(input("Please enter a valid value for x (The length of a sqaure packet)"))
if x < 10 and x >0:
    result = getValidSpecialOffer()
    if result == "y":
        additionalfreerows = int(input("How many additional free rows come with the offer?"))
    totalcans = (x * x) + additionalfreerows
    print(totalcans, "total cans")