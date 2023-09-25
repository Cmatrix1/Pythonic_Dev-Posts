from itertools import count

# Count starting from 1, with a step of 2
for num in count(1, 2):
    print(num)

# The output will be an endless list of consecutive odd numbers starting from 1: 1, 3, 5, 7, and so on.



from itertools import cycle

# Cycle through the elements of a list indefinitely
my_list = [1, 2, 3]
for element in cycle(my_list):
    print(element)
# This code will keep printing the elements 1, 2, 3, 1, 2, 3, and so on, in an infinite loop.



from itertools import repeat

# Repeat the number 42 four times
for num in repeat(42, 4):
    print(num)
# In this case, the output will be 42 printed four times, as specified.