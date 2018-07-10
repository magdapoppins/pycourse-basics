import csv

csv_file = open('csv_sample.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

# Skip first row if it only contains the column headers
next(csv_reader)
females = 0

for row in csv_reader:
    id, name, gender, dates, yearOfBirth, yearOfDeath, placeOfBirth, placeOfDeath, url = row
    print(name)
    if gender == 'Female':
        females += 1

print("Count of females was {}.".format(females))        


csv_file.close()