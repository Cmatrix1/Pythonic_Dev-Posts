
# Quizz 1
def reverse(s: list):
    s.reverse()
    return s

lst = [1, 2, 3]
lst2 = reverse(lst)
print(lst is lst2)


# Quizz 2
lst = [1, 2, 3, [1, 2]]
lst2 = list(lst)

print(id(lst[-1]) == id(lst2[-1]))
print(id(lst) == id(lst2))
print(id(lst[0]) == id(lst[0]))


# Quizz 3
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)
print(a == b)
print(a is c)
print(a == c)



#Quizz 4
lst = [1, 2, 3, 4]
lst2 = lst.copy()
print(id(lst[1]) == id(lst[1]))



# Quizz 5
lst = [1, 2, 3]
tpl = (1, 2, 3)
print(id(lst) == id(list(lst)))
print(id(tpl) == id(tuple(tpl)))


