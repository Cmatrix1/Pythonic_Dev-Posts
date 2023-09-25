# Task: Implement a program that reads data from a CSV file containing information about employees and their salaries. The program should calculate the average salary for each department and display the results.

# Requirements:

#     The CSV file should have the following columns: "Name", "Department", and "Salary".
#     Use named tuples to represent the employee records.
#     The program should read the CSV file and create a list of named tuples, where each named tuple represents an employee record.
#     Calculate the average salary for each department5. Display the department name and its corresponding average salary.


from collections import namedtuple

Employee = namedtuple("Employee", "name department salary")

file = open("test.csv")
lines = file.readlines()

employes = []
for line in lines[1:]:
    name, department, salary = line.replace("\n", "").split(",")
    employe: Employee = Employee(name, department, salary)
    employes.append(employe)

departments = {}
for employe in employes:
    if not employe.department in departments:
        departments[employe.department] = []
    departments[employe.department].append(int(employe.salary))


for departemtn, salarys in departments.items():
    print(f"{departemtn}: Average Salary = {sum(salarys) / len(salarys)}")
