#assuming there are no windows and doors, each wallpaper piece covers an area of 2m squared, same for the carpet, and 1 litre of paint covers 3 metres squared

length = int(input("Please enter the length of the room"))
breadth = int(input("Please enter the breadth of the room"))
height = int(input("Please enter the height of the room"))

floorarea = length * breadth
print(floorarea)
walls = (2 * length * height) + (2 * breadth * height)
numberofwallpaper = walls / 2
numberofcarpet = floorarea / 2
litresofpaint = walls / 3

print ("you will need", numberofwallpaper, "sheets of wallpaper, ", numberofcarpet, "pieces of carpet and", litresofpaint, "litres of paint")