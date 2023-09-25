

def my_function(iterator):
    for number in iterator:
        print(number)


numbers = [1, 2, 3]
iterator = iter(numbers)

my_function(iterator)
my_function(iterator)

print(next(iterator))



    # 1, 2, 3, 1, 2, 3, 1
    # 1, 2, 3
    # 1, 2, 3, StopIteration.
    # StopIteration.
