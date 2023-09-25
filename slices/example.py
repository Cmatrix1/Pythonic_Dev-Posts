# 1️⃣ Inserting Data:

my_list = [1, 2, 3, 4, 5]
my_list[2:2] = [10, 11, 12]
print(my_list)  # Output: [1, 2, 10, 11, 12, 3, 4, 5]


# 2️⃣ Deleting Data:

my_list = [1, 2, 3, 4, 5]
my_list[1:4] = []
print(my_list)  # Output: [1, 5]


# 3️⃣ Changing Data:

my_list = [1, 2, 3, 4, 5]
my_list[1:4] = [20, 30, 40]
print(my_list)  # Output: [1, 20, 30, 40, 5]


## Quizz


my_list = [1, 2, 3, 4, 5]
my_list[::2] = [-1, -3, -5, -7]
print(my_list)

[-1, 2, -3, 4, -5]
[-1, 2, -3, 4, -5, -7]
Error: ValueError