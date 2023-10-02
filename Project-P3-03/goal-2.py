from random import seed, choices
from collections import Counter

eye_colors = ("amber", "blue", "brown", "gray", "green", "hazel", "red", "violet")
class Person:
    def __init__(self, eye_color):
        self.eye_color = eye_color
    
    def __repr__(self):
        return f"Person({self.eye_color})"


seed(0)
persons = [Person(color) for color in choices(eye_colors[2:], k = 50)]


counter = Counter({color: 0 for color in eye_colors})
counter.update(person.eye_color for person in persons)
print(counter)