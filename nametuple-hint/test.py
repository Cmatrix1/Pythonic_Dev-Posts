

from collections import namedtuple

# Define the structure of the namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create an instance of Person
john = Person(name='John Doe', age=30, city='New York')

# Accessing values
print(john.name)  # Output: John Doe
print(john.age)   # Output: 30
print(john.city)  # Output: New York

print(john._asdict())