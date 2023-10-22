class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def __format__(self, format_spec):
        if format_spec == "fancy":
            return f"A fancy {self.make} {self.model}, priced at ${self.price:,}"
        else:
            return f"A {self.make} {self.model} with a price of ${self.price}"


my_car = Car("Tesla", "Model S", 80000)

print(f"My car: {my_car:fancy}")
print(f"Another car: {my_car}")
