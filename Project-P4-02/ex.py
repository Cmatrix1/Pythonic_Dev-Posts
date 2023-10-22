from functools import total_ordering


@total_ordering
class Mod:
    def __init__(self, modular, value):
        if not isinstance(value, int) and not isinstance(modular, int):
            return ValueError("The value and modular must be an integer")
        if modular < 0:
            return ValueError("The modular must be a positive integer")

        self._modular = modular
        self._value = value % modular

    def __str__(self):
        return f"Mod(modular={self._modular}, value={self._value})"

    def __repr__(self):
        return f"Mod(modular={self._modular}, value={self._value})"

    @property
    def modular(self):
        return self._modular

    @property
    def value(self):
        return self._value
    
    def get_value(self, value):
        if isinstance(value, Mod):
            return value.modular % self.modular
        elif isinstance(value, int):
            return value % self.modular
        raise ValueError("The Value should be integer or Mod instance")


    def __eq__(self, other):
        other = self.get_value(other)
        return self.modular == other
    
    def __le__(self, other):
        return self.modular < other.mod
        
        
    def __int__(self):
        return self.value

    def __mul__(self, other):
        other = self.get_value(other)
        return Mod(modular=self.modular, value=self.value * other)
    
    def __imul__(self, other):
        other = self.get_value(other)
        self._value *= other % self.modular 
        return self

    def __add__(self, other):
        other = self.get_value(other)
        return Mod(modular=self.modular, value=self.value + other)



test = Mod(3, 8)
print(test + 2)
print(test)
print(int(test))
print(Mod(3, 8) == Mod(3, 80))
test * 63
print(test * 63)
print(test > Mod(5, 29))