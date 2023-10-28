from types import FunctionType



class sadegh:
    def __init__(self, fget: FunctionType, fset: FunctionType=None, fdel: FunctionType=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner_class):
        return self.fget(instance)

    def __set__(self, instance, value):
        if not self.fset:
            raise TypeError("this property is read-only")
        return self.fset(value)
        
    def __set_name__(self, owner, name):
        self.property_name = name



class CustomPropertyTest:
    def get_name(self):
        return "Mohammad"

    name = sadegh(fget=get_name)

s = CustomPropertyTest()
print(s.name)

