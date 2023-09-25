

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}
def iter_dict(my_dict: dict) -> tuple:
    for key_value in my_dict.items():
        key, value = key_value
        yield key, value

method = iter_dict(my_dict)
print(next(method))
print(next(method))
print(next(method))
print(next(method))






# BEST PRACTICE
def fib(n: int) -> int:
    first = 0
    second = 1
    for _ in range(n):
        yield first
        first, second = second, first + second


# BAD PRACTICE
def fib(n):
    first = 0
    second = 1
    
    new_number = 0
    for _ in range(n):
        yield first
        new_number = first + second
        first = second
        second = new_number


a = 1
a, b = a+1, a+2
print(a, b)
