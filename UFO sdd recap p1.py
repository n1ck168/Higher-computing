# RECAP - UFO
# Original task by Mr Neil, adapted by Mr Simpson
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
import csv
thisDate = []
country = []
location = []
shape = []
description = []
filePath = ''

# -------------------------------------------------- DO NOT ALTER -----
def importFile():
    with open(filePath+'ufo_sighting.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            thisDate.append(row[0])
            country.append(row[1])
            location.append(row[2])
            shape.append(row[5])
            description.append(row[6])
    return thisDate, country, location, shape, description
# -------------------------------------------------- DO NOT ALTER -----


def countPerCountry(countryarray, specifiedcountry):
    numSightings = 0 
    for i in range (0,len(countryarray)):
        if countryarray[i] == specifiedcountry:
            numSightings = numSightings + 1
    return numSightings



def displaySightings(specifiedcountry, numSightings):
    print("There are", numSightings, "sightings that took place in", specifiedcountry)



def countyearsightings(numsightings, thisDate):
    numSightings = []
    count = 0
    #countposition = []
    for counter in range (0,len(thisDate)-1):
        currentyear = thisDate[counter][6:11]
        nextyear = thisDate[counter+1][6:11]
        if currentyear == nextyear:
            count = count + 1 
        else:
            numSightings.append(count)
            count = 0
    
    print(numSightings)
    # i = 0    
    # for i in range:
    #     print (countposition[i], countposition[i])
    #     i = i + 1     
          


# main program
thisDate, country, location, shape, description = importFile() # 1. ImportFile IN: none OUT: thisDate, country, location, shape, description
specifiedcountry = input("Please enter a country")
numSightings = countPerCountry(country, specifiedcountry) # 2. countPerCountry IN: country[], specifiedCountry OUT: numSightings
displaySightings(specifiedcountry, numSightings) #  3. displaySightings IN: specifiedCountry, numSightings OUT: none
countyearsightings(count, thisDate)
