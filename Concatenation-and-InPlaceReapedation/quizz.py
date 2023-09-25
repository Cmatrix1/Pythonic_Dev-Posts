
s1 = "@"
s2 = "Pythonic_Dev"

id_of_s1 = id(s1)
s1 += s2

print(id(s1) == id_of_s1)


l1 = [1, 2, 3]
l2 = [4, 5, 6]

id_of_l1 = id(l1)
l1 += l2

print(id(l1) == id_of_l1)



True, True
False, True
True, False
False, False