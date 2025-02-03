import csv

# Initialize lists
thisDate = []
country = []
location = []
shape = []
description = []
filePath = ''  # Ensure the CSV file is in the correct location

# -------------------------------------------------- DO NOT ALTER -----
def importFile():
    with open(filePath + 'ufo_sighting.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Skip header row if present
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
    for i in range(len(countryarray)):
        if countryarray[i].strip().lower() == specifiedcountry.strip().lower(): #compares them and remove the whitespaces at beginning and end of  string
            numSightings += 1
    return numSightings

def displaySightings(specifiedcountry, numSightings):
    print("There are", numSightings, "sightings that took place in", specifiedcountry)

def countyearsightings(thisDate):
    year_sightings = {}  # Dictionary to store year-wise sightings

    for date in thisDate:
        year = date[-4:]  # Extract last 4 characters assuming "MM/DD/YYYY"
        if year.isdigit():  # Ensure it's a valid year
            year_sightings[year] = year_sightings.get(year, 0) + 1

    print("\nSightings per year:")
    for year, count in sorted(year_sightings.items()):
        print(f"{year}: {count}") #f means can put it in this form rather than print(year":", count)

# Main program
thisDate, country, location, shape, description = importFile()  # Import Data
specifiedcountry = input("Please enter a country: ").strip()
numSightings = countPerCountry(country, specifiedcountry)  # Count sightings per country
displaySightings(specifiedcountry, numSightings)  # Display results
countyearsightings(thisDate)  # Count sightings per year