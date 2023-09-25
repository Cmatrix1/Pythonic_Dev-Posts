

def prime(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrapper

@prime
def test_gen():
    while True:
        word = yield
        print("This is My Word", word)

a = test_gen()
a.send(None)