def nested_generator():
    yield 'Hello'
    yield 'from'
    yield 'nested'
    yield 'generator'

def main_generator():
    yield from nested_generator()

for item in main_generator():
    print(item)

# Hello
# from
# nested
# generator