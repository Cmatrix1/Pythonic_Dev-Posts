from enum import Enum




class AppExceptions(Enum):
    NotAnIntenger = 100, ValueError, "The Value Is Not an Integer"
        
    @property
    def code(self):
        return self.value[0]
    
    def throw(self):
        raise self.exception(self.message)
    
    def __new__(cls, code, exception, message):
        member = object.__new__(cls)
        member._value_ = code
        member.message = message
        member.exception = exception
        return member

