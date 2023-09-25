def number_generator():
    yield 1
    yield 2
    yield 3
    return "Done"

gen = number_generator()

for number in gen:
    print(number)

# Output:
# 1
# 2
# 3

try:
    print(next(gen))
except StopIteration as e:
    print(e.value)  # Output: Done
