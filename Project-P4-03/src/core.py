


class Resource: 
    __slots__ = ("_name", "_manufacturer", "_total", "_allocated")

    def __init__(self, name: str, manufacturer: str, total: int, allocated: int):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
        self._allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    @property
    def category(self):
        return self.name.upper()


    def __str__(self):
        return f'{self.__class__.__name__}(name={self.name})'
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, _manufacturer={self.manufacturer}, total={self.total}, allocated={self.allocated}, category={self.category})'
    
    def claim(self, count):
        self._validate_integer(count)
        if self.total - count < 0:
            raise ValueError('We have no available resourse that much')
        
        self.total -= count

    def freeup(self, count):
        self._validate_integer(count)
        self.total += count
    
    def died(self):
        pass
    
    def purchased(self):
        pass

    @staticmethod
    def _validate_integer(count):
        if isinstance(count, int) and count > 0:
            return count
        raise ValueError("The Count Should Be Positive int")

res1 = Resource(name="tes", manufacturer="tes", total="tes", allocated="tes", category="tes")

