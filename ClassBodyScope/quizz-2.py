name = 'Guido'

class MyClass:
    name = 'Raymond'
    list_1 = [name] * 2
    list_2 = [name for _ in range(2)]

print(MyClass.list_1)
print(MyClass.list_2)


# ['Raymond', 'Raymond'], ['Raymond', 'Raymond']
# ['Guido', 'Guido'], ['Guido', 'Guido']
# ['Guido', 'Guido'], ['Raymond', 'Raymond']
# ['Raymond', 'Raymond'], ['Guido', 'Guido']