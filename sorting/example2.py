import operator

# Compare two numbers ⚖️
x = 10
y = 20
print(operator.eq(x, y))

# Logical AND 🔀
x = True
y = False
print(operator.and_(x, y))


lst = [1, 2, 3, 4, 5]
print(operator.getitem(lst, 2))


import operator

# Compare two numbers ⚖️
x = 10
y = 20
print(operator.eq(x, y))  # 😄 if x == y, 😢 otherwise

# Logical AND 🔀
x = True
y = False
print(operator.and_(x, y))  # 😄 if x and y are both True, 😢 otherwise

# Get the element at index 2 in the list `lst`
lst = [1, 2, 3, 4, 5]
print(operator.getitem(lst, 2))  # 3️⃣

# Get the `test` attribute of the object `obj`
obj = {"test": 10}
print(operator.attrgetter("test")(obj))  # 1️⃣0️⃣

# Get the length of the string `str`
str = "Hello, world!"
print(operator.length_hint(str))  # 1️⃣3️⃣

# Check if the object `obj` is callable
obj = callable
print(operator.is_callable(obj))  # 😄
operator.attrgetter("test")