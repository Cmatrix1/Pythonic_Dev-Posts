class Cities:
    def __init__(self):
        self._cities = ['New York', 'Newark', 'New Delhi', 'Newcastle']
    
    # Implementing the __len__ method to return the length of the cities list
    def __len__(self):
        return len(self._cities)
    
    # Implementing the __iter__ method to return an instance of the CityIterator class
    def __iter__(self):
        return self.CityIterator(self)
    
    class CityIterator:
        def __init__(self, city_obj):
            self._city_obj = city_obj
            self._index = 0

        # Implementing the __iter__ method to make the iterator object iterable
        def __iter__(self):
            return self

        # Implementing the __next__ method to iterate through the cities list
        def __next__(self):
            if self._index >= len(self._city_obj):
                raise StopIteration  # Raise StopIteration when all cities have been visited
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item
