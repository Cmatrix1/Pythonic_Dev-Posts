from inspect import getgeneratorlocals, getgeneratorstate


def gen1():
    for i in range(1, 5):
        yield i

def gen2():
    start = "start the using of gen1"
    yield start
    g = gen1()
    yield from g
    end = "end the using of gen1"
    yield end

a = gen2()
print(next(a))
print(next(a))
g = getgeneratorlocals(a)["g"]
g.close()
print("A state is ", getgeneratorstate(a))
print("G state is ", getgeneratorstate(g))
print(next(a))
# a.close()
# print(next(a))
print()