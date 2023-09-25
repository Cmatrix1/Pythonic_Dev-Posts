import copy

original_list = [1, 2, [3, 4]]
copied_list = copy.deepcopy(original_list)

# Modifying the copied_list
copied_list[0] = 5
copied_list[2][0] = 6

print("Original List:", original_list) # [1, 2, [3, 4]]
print("Copied List:", copied_list) # [5, 2, [6, 4]]