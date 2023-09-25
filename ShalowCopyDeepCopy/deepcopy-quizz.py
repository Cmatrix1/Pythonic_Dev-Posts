

from copy import copy, deepcopy


class MyClass:
    def __init__(self, a):
        self.a = a


x = [10, 20]

obj = MyClass(x)
print(x is obj.a)

cp_shallow = copy(obj)
print(cp_shallow.a is obj.a)

cp_deep = deepcopy(obj)
print(cp_deep.a is obj.a)
