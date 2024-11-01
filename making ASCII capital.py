def capitalisation():
    animal = input("Please enter an animal: ")
    firstletter = ord(animal[0]) - 32
    first = chr(firstletter)
    print(first + animal[1:1000])


capitalisation()