

class Custom:
    def __init__(self, lst: list[str], start_at:int = 0) -> None:
        self.lst = lst
        self.start_at = start_at

    def __iter__(self):
        return self.CustomIterator(self)
    
    class CustomIterator:
        def __init__(self, iterabel: 'Custom') -> None:
            self.n = iterabel.start_at
            self.lst = iterabel.lst

        def __iter__(self):
            return self

        def __next__(self) -> int:
            data = self.n
            self.n += 1
            return f"{str(data)}{self.lst[self.n % len(self.lst)]}"


infinit = Custom(["N", "S", "W", "E"])

for i in infinit:
    print(i)



# class InfiniteCyclicalIterator: ...

# iterator = InfiniteCyclicalIterator("cmatrix1")

# for item in iterator:
#     print(item)

# # OutPut:
# # c1
# # m2
# # a3
# # t4
# # r5
# # i6
# # x7
# # c8
# # m9
# # a10
# # ...
