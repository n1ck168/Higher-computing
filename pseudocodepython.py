
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