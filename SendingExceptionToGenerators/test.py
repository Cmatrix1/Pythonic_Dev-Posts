


def gen():
    test = yield 

    for i in range(10):
        yield i + test

a = gen()
next(a)
a.send(84)
print(next(a))
print(next(a))
a.throw(Exception())
print(next(a))

