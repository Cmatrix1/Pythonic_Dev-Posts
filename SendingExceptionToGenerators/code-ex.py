def my_generator():
    value = yield
    while True:
        print(f"Received: {value}")
        value = yield


gen = my_generator()  # Create a generator object
next(gen)  # Start the generator

gen.send("Hello")  # Send "Hello" to the generator
gen.send("World")  # Send "World" to the generator

gen.close()  # Stop the generator
