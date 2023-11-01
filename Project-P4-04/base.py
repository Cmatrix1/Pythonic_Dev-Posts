from abc import ABC, abstractmethod

class BaseValidator(ABC):
    def __init__(self, *_, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner_class, name):
        self.name = name

    def __set__(self, instance, value):
        value = self.validator(instance, value)
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner_class):
        if instance:
            return instance.__dict__.get(self.name)
        return self
    
    @abstractmethod
    def validator(self):
        ...


class IntegerField:
    def validator(self, instance, value):
        if not (isinstance(value, int) and self.min_value < value < self.max_value):
            raise ValueError(f"Value must be integer and between {self.min_value} and {self.max_value}")


class StringField:
    def validator(self, instance, value):
        if not (isinstance(value, str) and self.min_value < len(value) < self.max_value):
            raise ValueError(f"Value must be integer and between {self.min_value} and {self.max_value}")
