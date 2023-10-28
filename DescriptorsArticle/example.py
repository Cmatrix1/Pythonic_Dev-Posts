# from datetime import datetime


# class TimeUTC:
#     def __get__(self, instance, owner_class):
#         return datetime.utcnow().isoformat()


# class Logger:
#     current_time = TimeUTC()


# print(Logger.__dict__)
# {'__module__': '__main__', 'current_time': <__main__.TimeUTC object at 0x0000019C24602390>,
#  '__dict__': <attribute '__dict__' of 'Logger' objects>,
#  '__weakref__': <attribute '__weakref__' of 'Logger' objects>, '__doc__': None}


class Choice:
    def __init__(self, *choices):
        self.choices = choices
        
    def __get__(self, instance, owner_class):
        return choice(self.choices)
    
    
from random import choice, seed

class Person:
    status = Choice('😃', '😄', '😊', '😉', '😍', '🤩', '😎', '🥳', '😇', '🙌')
    favorite_color = Choice('🔴', '🟠', '🟡', '🟢', '🔵', '🟣', '🟤', '⚫', '⚪', '🌈')


for i in range(10):
    print(Person.status)