
start = 2
stop = 100000000

primes = (
    i
    for i in range(start, stop)
        if not 
            [a for a in range(2, i) if i % a == 0]
)

for i in primes:
    print(i)



# start = 2
# stop = 100000000

# primes = [
#     i
#     for i in range(start, stop)
#         if not 
#             [a for a in range(2, i) if i % a == 0]
# ]

# for i in primes:
#     print(i)