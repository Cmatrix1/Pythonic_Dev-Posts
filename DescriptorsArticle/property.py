


class User:
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = str(value)

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = int(value)