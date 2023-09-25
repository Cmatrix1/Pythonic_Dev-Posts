students = [
    {'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'name': 'Bob', 'age': 19, 'grade': 'B'},
]

# Sort students based on their age in descending order
sorted_students_age = sorted(students, key=lambda x: x['age'], reverse=True)
print(sorted_students_age)
# Output
# [{'name': 'Charlie', 'age': 21, 'grade': 'C'},
#  {'name': 'Alice', 'age': 20, 'grade': 'A'}]
