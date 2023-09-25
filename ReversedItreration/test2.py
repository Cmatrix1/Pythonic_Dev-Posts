


from collections.abc import Iterator


class CustomIterator(Iterator):
    def __next__(self):
        return str(super().__next__())

class BadList(list):

    def __iter__(self) -> CustomIterator:
        print("___ITER___")
        # iterator = CustomIterator(self)
        # print(iterator.__next__(), "sadegh")
        # print("NEXT")
        # return iter(['1', "2", "3"])

    # def __getitem__(self, index):
    #     print("___GETITEM___")
    #     value = super().__getitem__(index)
    #     if index % 2 == 0:
    #         prefix = "even"
    #     else:
    #         prefix = "odd"
    #     return f"[{prefix}] {value}"


a = BadList((1, 2, 3, 5, 6, 7))
print(" ".join(a))