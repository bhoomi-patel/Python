# bill splitter

people = int(input("Enter number of people: "))
bill = float(input("Enter total bill amount: ₹"))

if people>0 :
    print("Each Person should pay: ₹",bill/people) 
else:
    print("Invalid number of people. Please enter a positive integer.")