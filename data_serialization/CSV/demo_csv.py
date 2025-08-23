import csv 

# method 1 : basic writer
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
]
with open('people.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# method 2 : using DictWriter
people = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
]
with open('people.csv','w',newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(people)

# method 3 : reading CSV file
with open('people.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# method 4 : reading CSV file using DictReader
with open('people.csv','r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)