# Creating two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Updating set1 with set2 using the | operator
set1 |= set2
print(set1) # Output: {1, 2, 3, 4, 5}


# Updating set1 with the intersection of set1 and set2 using the &= operator
set1 &= set2
print(set1) # Output: {3}


# Updating set1 with the difference of set1 and set2 using the -= operator
set1 -= set2
print(set1) # Output: {1, 2}


# Updating set1 with the symmetric difference of set1 and set2 using the ^= operator
set1 ^= set2
print(set1) # Output: {1, 2, 4, 5}

