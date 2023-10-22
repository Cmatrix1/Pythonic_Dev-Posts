# classmethod
class Employee:
    num_of_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.num_of_employees += 1

    @classmethod
    def get_total_employees(cls):
        return cls.num_of_employees

e1 = Employee("Alice")
e2 = Employee("Bob")

print(Employee.get_total_employees())  # Output: 2


# staticmethod
class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(MathUtil.add(5, 3))       # Output: 8
print(MathUtil.multiply(5, 3))  # Output: 15
