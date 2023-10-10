

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


pr = Person("Mr.Test", 18)

Person.say_hi = lambda self: print(self.name, "hi")
pr.say_hi()

pr.say_bye = lambda self: print(self.name, "bye")
pr.say_bye()


# what is the output?
# Mr.Test hi, Mr.Test bye
# None hi, None bye
# ERROR, ERROR 
# Mr.Test hi, Error