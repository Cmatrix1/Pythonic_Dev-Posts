from itertools import islice

# Assume `number_iterator` represents the sequence of numbers
number_iterator = iter(range(1, 1000001))

# Selectively slice the first 100 values
sliced_iterator = islice(number_iterator, 100)

# Now, we can process the sliced iterator:
for num in sliced_iterator:
    # Process each number as desired
    print(num)
