


# class Test:
#     def __init__(self, length) -> None:
#         self.length = length


#     def __iter__(self):
#         return TestItreator(self)
    
#     def __next__(self):
#         if self.n <= self.test.length:
#             self.n += 1
#             return self.n
#         raise StopIteration


# class TestItreator:
#     def __init__(self, test: Test) -> None:
#         self.test = test
#         self.n = 0

#     def __next__(self):
#         if self.n <= self.test.length:
#             self.n += 1
#             return self.n
#         raise StopIteration


# a = Test(10)

# for i in a:
#     print(i)


class Test:
    def __init__(self, length) -> None:
        self.length = length
        self.n = 0
    def __getitem__(self, i):
        if self.length >= self.n:
            self.n += 1
            return self.n
        raise IndexError
    
a = Test(10)
print()
for i in iter(a):
    print(i)
