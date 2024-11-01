#Create Python code to ask the user to enter a secure, valid password. The program should check that the first letter of the password entered 
# is a capital letter, then check that the last character is one of the following symbols: #, $ or %.

#The program should repeatedly ask the user to enter a secure password until they successfully do so. Please include helpful error messages.

def isCapital(letter):
    if ord(letter) > 90:
        print("error, the first letter of your password needs to be a capital")
        return False
    else:
        return True

def lastSymbol(lastletter):
    if not lastletter  == "#" and not lastletter == "$" and not lastletter == "%":
        print("error, your password must end in one of the following characters: $, #, %")
        return False
    else:
        return True

OriginalPas = input("Please enter a secure passoword")
print(ord(OriginalPas[0]))
lastletter =  (OriginalPas[len(OriginalPas)-1:len(OriginalPas)])

while not isCapital(OriginalPas[0]) or not lastSymbol(lastletter):
    OriginalPas = input("Please enter a secure passoword")
    print(ord(OriginalPas[0]))
    lastletter =  (OriginalPas[len(OriginalPas)-1:len(OriginalPas)])

print("All ok")