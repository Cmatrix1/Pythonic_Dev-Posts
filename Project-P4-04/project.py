from abc import ABC, abstractmethod


class IntegerField:
    def __init__(self, *_, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner_class, name):
        self.name = name

    def __set__(self, instance, value):
        print("set running")
        if not (isinstance(value, int) and self.min_value < value < self.max_value):
            raise ValueError(f"Value must be integer and between {self.min_value} and {self.max_value}")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner_class):
        if instance:
            return instance.__dict__.get(self.name)
        return self
    

class StringField:
    def __init__(self, *_, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner_class, name):
        self.name = name

    def __set__(self, instance, value):
        if not (isinstance(value, str) and self.min_value < len(value) < self.max_value):
            raise ValueError(f"Value must be integer and between {self.min_value} and {self.max_value}")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner_class):
        if instance:
            return instance.__dict__.get(self.name)
        return self






class Person:
    age = IntegerField(min_value=0, max_value=10)

