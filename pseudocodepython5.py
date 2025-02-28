#Challenge 5:

#An outline ASCII image can be made just using symbols for the outline and spaces elsewhere.
#For this batch of images, the first and last line must be entirely made of non-space symbols. The remaining lines must each contain exactly two non-space symbols, to mark the left and right side of the outline, but contain spaces for all other characters.
#Acceptable outline ASCII images, of a factory and a sand timer, are shown below.
#Input a single positive whole number to specify how many lines the image will contain. Then input that number of lines.
#Output the number of symbols, excluding spaces, that have been used to make the image.

#Pseudocode
#1. Ask for and store a valid  single positive whole number
#2. Set up an empty array called lines
#3. Loop length of lines array times
#4. Ask for and store line as a new item in the lines array
#5. End Loop
#6. Calculate number of symbols excluding spaces
# 6.1 Set count to 0
# 6.2 Loop for each line in the lines array
# 6.3      Loop for each character in the current line
# 6.4           If current character is not a space then
# 6.5                Increment count by 1
# 6.6           End if
# 6.7       End loop
# 6.8 End loop
# 7. Output number of symbols

counter = 0
positivenumber = int(input("Please enter the number of lines in the image: "))
while positivenumber < 0:
    print("This is not a valid number of lines")
    positivenumber = int(input("Please enter the number of lines in the image: "))
lines = [] 
for counter in range (0,positivenumber -1):
    x= input("Please enter line number", counter)
    lines.append(x)
    
