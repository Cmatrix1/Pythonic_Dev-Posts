#Quizz 1
# a = 1


lst = []
for i in range(6):
    lst.append(i)

print(i) # output: 5


lst2 = [a for a in range(6)]
# print(a) # ???



# Quizz 2
funcs = [lambda x: x**0, lambda x: x**1, lambda x: x**2, lambda x: x**3]

print(funcs[0](10)) # output: 1
print(funcs[1](10)) # output: 10
print(funcs[2](10)) # output: 100
print(funcs[3](10)) # output: 1000


funcs = [lambda x: x**i for i in range(6)]

print(funcs[0](10)) # output: ??
print(funcs[1](10)) # output: ??
print(funcs[2](10)) # output: ??
print(funcs[3](10)) # output: ??

1