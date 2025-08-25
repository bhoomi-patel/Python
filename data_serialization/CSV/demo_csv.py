# import csv 

# # method 1 : basic writer
# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', 30, 'New York'],
#     ['Bob', 25, 'Los Angeles'],
# ]
# with open('people.csv','w',newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# # method 2 : using DictWriter
# people = [
#     {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
#     {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
# ]
# with open('people.csv','w',newline='') as file:
#     fieldnames = ['Name', 'Age', 'City']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(people)

# # method 3 : reading CSV file
# with open('people.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
# # method 4 : reading CSV file using DictReader
# with open('people.csv','r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

# Problem 1: Employee Salary Analysis
# Given employees.csv with columns: name, department, salary, join_date
# Find the average salary per department and save to dept_averages.csv

import csv 
from collections import defaultdict

def analyze_salary(input_file,output_file):
    dept_data = defaultdict(list)
    with open(input_file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = row['department']
            salary = float(row['salary'])
            dept_data[dept].append(salary)
    # calculate averages
    dept_avg = []
    for dept,salary in dept_data.items():
        avg_salary = sum(salary)/len(salary)
        dept_avg.append({
            'department':dept,
            'employee_count':len(salary),
            'average_salary':round(avg_salary,2),
            'total_salary':sum(salary)
                         })
    with open(output_file,'w',newline='') as f:
        fieldnames = ['department','employee_count','average_salary','total_salary']
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dept_avg)
analyze_salary('employees.csv','dept_averages.csv')