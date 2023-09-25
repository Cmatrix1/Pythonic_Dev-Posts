# Task: Implement a custom iterator class called Squares that generates an infinite sequence of perfect squares (1, 4, 9, 16, 25, etc.) up to a given limit. The limit should be a parameter when creating an instance of the iterator.

# Requirements:

#     The Squares iterator should be created with a single parameter, limit, which indicates the maximum value of the squares to generate.
#     The iterator should start generating squares from 1 and continue indefinitely until reaching or exceeding the specified limit.
#     The __next__() method should return the next square in the sequence.
#     The iterator should raise a StopIteration exception when the limit is reached.



class Squares:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.number = 1
        self.times = 1
    
    def gen_number(self):
        self.number = self.times * self.times 
        self.times += 1
        return self.number
    
    def __next__(self):
        if self.times < self.limit:
            return self.gen_number()
        raise StopIteration("")

test = Squares(2)
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))