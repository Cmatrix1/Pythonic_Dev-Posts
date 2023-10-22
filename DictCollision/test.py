from timeit import timeit


class Number:
    def __init__(self, x):
        self.x = x
        
    def __eq__(self, other:'Number'):
        return self.x == other.x
    
    def __hash__(self):
        return hash(self.x)   

class SameHash:
    def __init__(self, x):
        self.x = x
        
    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        return 100
    

numbers = {Number(i): 'some value' for i in range(10_000)}
same_hashes = {SameHash(i): 'some value' for i in range(10_000)}

print(timeit('numbers[Number(500)]', globals=globals(), number=100_000)) # 0.02600
print(timeit('same_hashes[SameHash(500)]', globals=globals(), number=100_000))  # 2.64293