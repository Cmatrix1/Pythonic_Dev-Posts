

class CustomMutableString:
    pass



# Create a CustomMutableString object
string1 = CustomMutableString("Hello")

# Concatenate two CustomMutableString objects
string2 = string1 + CustomMutableString(" World")
print(string2)  # Output: "Hello World"

# Modify the original CustomMutableString object by concatenating it with another string
string1 += "!"
print(string1)  # Output: "Hello!"

# Repeat a CustomMutableString object
string3 = string2 * 3
print(string3)  # Output: "Hello WorldHello WorldHello World"

# Modify the original CustomMutableString object by repeating it
string2 *= 2
print(string2)  # Output: "Hello WorldHello World"

# Repeat a CustomMutableString object
string3 = 3 * string2
print(string3)  # Output: "Hello WorldHello WorldHello World"

# Check if a substring is present in a CustomMutableString object
print("World" in string2)  # Output: True
print("Python" in string2)  # Output: False
