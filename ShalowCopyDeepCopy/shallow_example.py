original_list = [1, 2, [3, 4]]

# Using slicing
sliced_copy = original_list[:]

# Using the .copy() method
method_copy = original_list.copy()

# Using the copy module
import copy
module_copy = copy.copy(original_list)

# Using the list() constructor
constructor_copy = list(original_list)


