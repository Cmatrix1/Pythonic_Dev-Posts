
# Iterable
lst = [1, 2, 3, 4, 5]
print("__iter__" in dir(lst)) # True
print("__next__" in dir(lst)) # False
print(iter(lst) is lst) # False


# Iterator
lst_iterator = iter(lst)
print("__iter__" in dir(lst_iterator)) # True
print("__next__" in dir(lst_iterator)) # True
print(iter(lst_iterator) is lst_iterator) # True

