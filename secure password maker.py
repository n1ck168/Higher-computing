#Create Python code to ask the user to enter a secure, valid password. The program should check that the first letter of the password entered 
# is a capital letter, then check that the last character is one of the following symbols: #, $ or %.

#The program should repeatedly ask the user to enter a secure password until they successfully do so. Please include helpful error messages.

OriginalPas = input("Please enter a secure passoword")
while ord(OriginalPas[0]) < 65:
    print("error, the first letter of your password needs to be a capital")
    OriginalPas = input("Please enter a secure password")
while str(OriginalPas(-1)) not == "#" or not == "$" or not == "%"
    print("error, your password must end in one of the following characters: $, #, %")
    OriginalPas = input("Please enter a secure password")

