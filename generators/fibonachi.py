

def fib(n) -> int:
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a

x = fib(20)
for c in x:
    print(c)
