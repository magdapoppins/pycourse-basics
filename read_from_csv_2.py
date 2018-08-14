import csv

csv_file = open("../../trees.csv")
csv_reader = csv.reader(csv_file, delimiter=',')

for row in csv_reader:
    index, grith, height, volume = row
    print(height)


csv_file.close()    
