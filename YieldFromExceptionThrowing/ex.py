def subgenerator():
    while True:
        try:
            x = yield
        except ValueError as e:
            print(f"Caught exception in subgenerator: {e}")

def delegating_generator():
    g = subgenerator()
    yield from g  # Delegates to subgenerator
    g.close()     # Closes subgenerator when done delegating

gen = delegating_generator()
next(gen)  # To prime the generator

gen.throw(ValueError("Exception thrown from delegating generator"))
# OutPut: Caught exception in subgenerator: Exception thrown from delegating generator
