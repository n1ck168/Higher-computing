
#Challenge 1:
#A lot of action can occur in the second-half of a hockey match as teams get tired.
#Input the half-time score as 2 whole numbers on 2 separate lines.
#Input the full-time score as 2 whole numbers on 2 separate lines.
#Output the number of goals scored after the half-time break.

#Pseudocode:
#1. Ask for and store home team half time score
#2. Ask for and store away team half time score
#3. Ask for and store hone team full time score
#4. Ask for and store away team full time score
#5. Calculate the total number of goals scored after the half time break
#6. Output the number of goals scored after the half time break

#Python:
halftimeHome = int(input("What was the score for the home team after half time?: "))
halftimeaway = int(input("What was the score for the away team after half time?: "))
fulltimehome = int(input("What was the score for the home team after full time?: "))
fulltimeaway = int(input("What was the score for the away team after full time?: "))

awayafterhalf = fulltimeaway - halftimeaway
homeafterhalf = fulltimehome - halftimeHome
totalafterhalf = homeafterhalf + awayafterhalf
print(totalafterhalf)

#Challenge 2:
#For a circus act, chairs of a certain type can be stacked as shown in which pairs of chairs fit together with one rotated.
#In this situation with 2 chairs there are 8 chair legs for every chair height.
#Other pairs of chairs are then stacked directly on top to form a tower so that every pair of chairs that the tower gets higher adds another 8 further chair legs.
#Input the height of one chair in cm.
#Input also the overall height of the stacked pair tower in cm.
#Output the total number of chair legs present in the tower.

#Pseudocode:
#1. Ask for and store height of one chair in cm
#2. Ask for and store height of the stacked tower in cm
#3. Calculate total number of chair legs in tower
#4. Output total number of chair legs in tower

#Python:
heightofchair = int(input("Please enter the height of one chair in centimeters: "))
heightoftower = int(input("Please enter the height of the tower in centimeters: "))
numberofchairshigh = heightoftower / heightofchair
numberofchairlegs = numberofchairshigh * 8
print(numberofchairlegs) 

#Challenge 3:
#Everyone likes as many Saturdays as possible in a year.
#A year has 365 days unless it is a leap year which gives it an extra day.
#The number of Saturdays in a year can be calcuated from the day of the week which 1st January lies on and whether it is a leap year or not.
#Input the week day for January 1st in uppercase two letter format (MO / TU / WE / TH / FR / SA / SU).
#Also input whether it is a leap year or not as y (for yes) or n (for no).
#Output the number of Saturdays which that year will contain

#Pseudocode: 
#1.1 Ask for and store Week day for January 1st (two letter format: MO/TU/WE...)
#1.2. While january1stday and _ Do
#1.3.       Output error message
#1.4.       Ask for and store _____________
#1.5. End While
#2. Ask for and store date of jan first and if its a leap year or not
#3. Calculate numberofsaturdays
#4. Output year with most saturdays / how many said year has






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
#     Ask for and store a valid deal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
#    If y then
#        Ask for and store the number of additional rows included for free
#Calculate numberoffreerows
#Output numberoftincans

x = int(input("Please enter a valid value for x (The length of a sqaure packet)"))
if len(x) = 1:
    import random
    number = random.randint(1,2) 
    if number = 1:
        discount = "no"
    if number = 2:
        discount = yes
