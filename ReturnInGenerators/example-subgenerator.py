def subgenerator():
    yield "Hello"
    yield "from"
    yield "subgenerator"
    return "End of subgenerator"

def delegator():
    yield "Start of delegator"
    result = yield from subgenerator()
    yield "Received from subgenerator: " + result
    yield "End of delegator"

gen = delegator()
            
for item in gen:
    print(item)

# Output:
# Start of delegator
# Hello
# from
# subgenerator
# Received from subgenerator: End of subgenerator
# End of delegator

