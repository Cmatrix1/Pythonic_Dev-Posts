

class CustomMutableString:
    def __init__(self, initial_string: str):
        """
        Initialize a CustomMutableString object with an initial string.

        Args:
            initial_string (str): The initial string value for the CustomMutableString object.
        """
        self.string = initial_string

    def __repr__(self) -> str:
        return self.string

    def __add__(self, other: 'CustomMutableString') -> 'CustomMutableString':
        """
        Concatenate two CustomMutableString objects and return a new CustomMutableString object.

        Args:
            other (CustomMutableString): The CustomMutableString object to concatenate with.

        Returns:
            CustomMutableString: A new CustomMutableString object resulting from the concatenation.
        """
        if isinstance(other, CustomMutableString):
            return CustomMutableString(self.string + other.string)
        elif isinstance(other, str):
            return CustomMutableString(self.string + other)

    def __iadd__(self, other: 'CustomMutableString') -> 'CustomMutableString':
        """
        Concatenate another CustomMutableString object to the current object in-place.

        Args:
            other (CustomMutableString): The CustomMutableString object to concatenate with.

        Returns:
            CustomMutableString: The modified CustomMutableString object after concatenation.
        """
        if isinstance(other, CustomMutableString):
            self.string += other.string
        elif isinstance(other, str):
            self.string += other
        return self
        

    def __mul__(self, n: int) -> 'CustomMutableString':
        """
        Duplicate the CustomMutableString object n times and return a new CustomMutableString object.

        Args:
            n (int): The number of times to duplicate the CustomMutableString object.

        Returns:
            CustomMutableString: A new CustomMutableString object resulting from duplication.
        """
        return CustomMutableString(self.string * n)

    def __imul__(self, n: int) -> 'CustomMutableString':
        """
        Duplicate the current CustomMutableString object n times in-place.

        Args:
            n (int): The number of times to duplicate the CustomMutableString object.

        Returns:
            CustomMutableString: The modified CustomMutableString object after duplication.
        """
        self.string *= n
        return self

    def __rmul__(self, n: int) -> 'CustomMutableString':
        """
        Duplicate the CustomMutableString object n times when it is on the right side of the multiplication operator.

        Args:
            n (int): The number of times to duplicate the CustomMutableString object.

        Returns:
            CustomMutableString: A new CustomMutableString object resulting from duplication.
        """
        return CustomMutableString(self.string * n)
    
    def __contains__(self, substring: str) -> bool:
        """
        Check if the given substring is present in the CustomMutableString object.

        Args:
            substring (str): The substring to search for.

        Returns:
            bool: True if the substring is found, False otherwise.
        """
        if isinstance(substring, CustomMutableString):
            return substring.string in self.string
        elif isinstance(substring, str):
            return substring in self.string
        raise TypeError("The Substring Should be 'str' or 'CustomMutableString'")
    

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