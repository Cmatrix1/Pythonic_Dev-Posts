from weakref import WeakKeyDictionary

class IntegerField:
    def __init__(self, max_value=None, min_value=None):
        self.max_value = max_value
        self.min_value = min_value
        self.storage = WeakKeyDictionary()

    def __get__(self, obj, class_obj):
        print(self.storage.keyrefs())
        if obj is None:
            return self
        return self.storage.get(obj)
        

    def __set__(self, obj, value):
        if not (self.min_value <= value < self.max_value):
            raise ValueError(f'The value must be greater than {self.min_value} and less than {self.max_value}')
        self.storage[obj] = value
        


class Boy:
    age = IntegerField(max_value=30, min_value=18)
    height = IntegerField(max_value=210, min_value=140)

    def __init__(self, age, height) -> None:
        self.height = height
        self.age = age    

class Girl:
    age = IntegerField(max_value=30, min_value=18)
    height = IntegerField(max_value=200, min_value=130)

    def __init__(self, age, height) -> None:
        self.height = height
        self.age = age


sadegh = Boy(age=18, height=193)
ali = Boy(age=28, height=173)
# mamad = Boy(age=29, height=203)
# afareen = Girl(age=18, height=165)
# fateme = Girl(age=19, height=175)



print(sadegh.age)

del sadegh
print(ali.age)
