

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.iterator = None
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        try:
            value = self.data[self.index]
            self.index += 1
            return value
        except TypeError:
            if not self.iterator:
                self.iterator = iter(self.data)
            return next(self.iterator)


a = {1, 2, 3, 4, 5}
for i in MyIterator(a):
    print(i)


a = [1, 2, 3, 4, 5]
for i in MyIterator(a):
    print(i)