def subgenerator():
    try:
        for i in range(10):
            word = yield None
            print(word)
    except ZeroDivisionError:
        print("I get it in subgeneratorlcs")
        return 2

def delegator():
    result = yield from subgenerator()
    print(result)
    yield 
a = delegator()
next(a)
a.send("salam")
a.throw(ZeroDivisionError)

a.close()