temperatures = []

with open("temperature.txt") as readfile:
    temp = readfile.readline().strip()
    while temp != "":
        temperatures.append(int(temp))
        temp = readfile.readline().strip()

print(temperatures)
totaltemp = 0
for i in range (len(temperatures)):
    totaltemp += temperatures[i]
averagetemp = totaltemp / len(temperatures)
print(averagetemp)
