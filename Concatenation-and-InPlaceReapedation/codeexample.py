

# 1️⃣ Concatenation:
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2
print(result)  # Output: Hello World

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# 2️⃣ In-Place Concatenation:
string = "Hello"
string += " World"
print(string)  # Output: Hello World

list = [1, 2, 3]
list += [4, 5, 6]
print(list)  # Output: [1, 2, 3, 4, 5, 6]

# 3️⃣ In-Place Repetition:
string = "Hello"
string *= 3
print(string)  # Output: HelloHelloHello

list = [1, 2]
list *= 4
print(list)  # Output: [1, 2, 1, 2, 1, 2, 1, 2]