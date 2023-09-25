

class Arithmetic:
    def __init__(self, n: int) -> None:
        self.n = n

    # def __len__(self):
    #     return self.n

    def __getitem__(self, s):
        if isinstance(s, slice):
            return [
                self.__getitem__(i)
                for i in
                (s.start or 0, s.stop, s.step or 1)
            ]
        elif isinstance(s, int):
            if s < 0:
                s += self.n
            if s >= 0 and s < self.n:
                # plus 1 because our sequence starts at 2
                return Arithmetic.get_number(s+1)
        raise IndexError

    @staticmethod
    def get_number(number: int) -> int:
        return (number * 3) - 1


sequence = Arithmetic(5)
print(list(sequence))
print(sequence[-4:-1:1])

print(tuple(sequence))
print(set(sequence))

for i in sequence:
    print(i)
