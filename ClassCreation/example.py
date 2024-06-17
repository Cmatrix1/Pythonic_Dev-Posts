import math

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
    def area(self):
        return math.pi * self.r ** 2
    

print(type(Circle))
# <class 'type'>


class_name = 'Circle'
class_body = """
def __init__(self, x, y, r):
    self.x = x
    self.y = y
    self.r = r

def area(self):
    return math.pi * self.r ** 2
"""
class_bases = ()  # defaults to object
class_dict = {}
Circle = type(class_name, class_bases, class_dict)

print(Circle)
# __main__.Circle
