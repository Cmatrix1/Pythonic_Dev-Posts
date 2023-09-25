
def my_generator():
    try:
        while True:
            yield
    except GeneratorExit:
        print("Generator closed!")

gen = my_generator()
next(gen)
gen.close()


def my_generator():
    try:
        while True:
            yield
    except Exception as e:
        print(f"Exception caught: {e}")

gen = my_generator()
next(gen)
gen.throw(ValueError("Oops, something went wrong!"))
